# Databricks notebook source
import requests
from pyspark.sql import SparkSession
from datetime import datetime
from pyspark.sql.types import StructType, StructField, StringType, DateType, BooleanType

# 1. Set Up API
auth_url = "https://icdaccessmanagement.who.int/connect/token"
api_url = "https://id.who.int/icd/release/10/2019/A00-A09"
client_id = '9f374f1d-104a-4385-9102-3e7fa8c92619_1f4664aa-d6ec-43af-9fac-a15396381287' 
client_secret = 'Q7TL7vO1GRC0uK3GIsR/4gbfDq9OrIwi5Hu/wLmKMAE='

# 2. Authenticate with WHO ICD API
auth_payload = {
    "client_id": client_id,
    "client_secret": client_secret,
    #"scope": "icdapi_access",
    "grant_type": "client_credentials"
}

auth_response = requests.post(auth_url, data=auth_payload)
if auth_response.status_code == 200:
    access_token = auth_response.json().get("access_token")
    print("Successfully authenticated!")
else:
    raise Exception(f"Authentication failed: {auth_response.status_code} - {auth_response.text}")

# 3. Fetch ICD-10 Data
headers = {
    "Authorization": f"Bearer {access_token}",
    "API-Version": "v2",
    "Accept": "application/json",
    "Accept-Language": "en"
}

response = requests.get(api_url, headers=headers)
if response.status_code == 200:
    icd_data = response.json()
    print("Successfully fetched ICD-10 data!")
else:
    raise Exception(f"Failed to fetch ICD data: {response.status_code} - {response.text}")

# 4. Process and Convert Data to Spark DataFrame
current_date = datetime.now().date()
children = icd_data.get("child", [])
data = []
for child_url in children:
    child_response = requests.get(child_url, headers=headers)
    if child_response.status_code == 200:
        child_data = child_response.json()
        data.append({
            'icd_code': child_data.get('code', 'Unknown'),
            'icd_code_type': 'ICD-10',
            'code_description': child_data.get('title', {}).get('@value', 'Unknown'),
            'inserted_date': current_date,
            'updated_date': current_date,
            'is_current_flag': True
        })
    else:
        print(f"Failed to fetch child data: {child_response.status_code} - {child_response.text}")

# Convert to Spark DataFrame and Define the schema explicitly
schema = StructType([
    StructField("icd_code", StringType(), True),
    StructField("icd_code_type", StringType(), True),
    StructField("code_description", StringType(), True),
    StructField("inserted_date", DateType(), True),
    StructField("updated_date", DateType(), True),
    StructField("is_current_flag", BooleanType(), True)
])
if data:
    df = spark.createDataFrame(data,schema=schema)
    print("ICD data successfully converted to Spark DataFrame!")
else:
    raise Exception("No data available to process.")

# 5. Write DataFrame to Azure Data Lake in Parquet Format
dbutils.fs.mounts()
df.write.format("parquet").mode("append").save("/mnt/bronze/icd_codes/")
print(f"ICD-10 data successfully written to Azure Data Lake")
display(df)

