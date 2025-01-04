# Azure-Data-Platform
Technology - Azure Data Engineering Stack; Domain - Healthcare Revenue Cycle Management (RCM)

RCM is the process that hospitals use to manage the financial aspects, from the time the patient schedules an appointment till the time the provider gets paid. Here is a simplified breakdown:
1.It starts with a patient visit: patient details and insurance details are collected by the hospital or clinic. This ensure the provider knows who will pay for the services, insurance, the patient, or both will pay for it.
2. Services are provided.
3. Billing happens: The hospital will create a bill.
4. Claims are reviewed: Insurance company will review the bill. It might accept it, pay in full or partial or decline.
5. Payments and follow-ups. If partial payment is done by insurance company, then some portion is given by the patient, and the provider will follow up for the payment.
6. Tracking and improvement. The hospital will monitor the process.

RCM ensures the hospital can provide quality care while also staying financially healthy. 

As part of RCM we have 2 main aspects: 
- Accounts Receivable (AR): The money the provides receive.  https://mdmanagementgroup.com/healthcare-accounts-receivable-management/
- Accounts Payable: The money the provides pay.

Patient paying is often a risk. Scenarios when patient has to pay:
Low Insurance - These insurance provides put most of the burden on patients.
Private Clinics
Deductibles

2 objectives for AR
-Bring cash
-also minimize the collection period

KPIs to measure AR and set benchmarks: https://gentem.com/blog/revenue-cycle-kpis-definitions-and-benchmarks/
1. AR > 90 days
2. Days in AR
3. etc

Datasets
==========
1. EMR Data - Electronic Medical Records (Azure SQL DB)
    - Patients
    - HCP/Providers
    - Department
    - Transactions
    - Encounter 

    Hospital a - Azure SQL DB
    Hospital b - Azure SQL DB
    
2. Claims Data - Insurance company / payer (flat files) 
    - folder in Data Lake - Landing (monthly once)
    
3. NPI Data - National Provider Identifier / Provider data (Public API)

4. ICD Data - ICD codes are a standardized system used by health care providers to map diagnosis code and description. CPT codes are Current Procedural Terminology codes.In plain language, CPT codes describe clinical procedures and diagnostic and care activities in the healthcare system. (API)

5. CPT Data - ICD codes, aka International Classification of Disease codes, describe the client’s diagnosis. (flat files)
   In other words, they refer to the specific condition that’s being treated, such as attention-deficit disorder (ADHD), predominantly inattentive type or generalized anxiety disorder (GAD).

note: difference between ICD codes and CPT codes:
https://www.simplepractice.com/blog/icd-codes-and-cpt-codes/

Solution/Medallion Architecture
=====================================
landing    -> bronze        -> silver       -> gold
flat files -> parquet files -> Delta tables -> Delta tables

bronze - source of truth (Data Engineer)
silver - data cleaning, enrich, common data model (CDM), SCD2 (Data Scientist, Machine Learning, Data Analyst)
gold - aggregation, fact and dimension tables for reporting (Business Users)

Tools - Azure Data Factory (data ingestion), Azure Databricks (data processing), Azure SQL Database, Azure Storage Account, Azure Key Vault

https://github.com/user-attachments/assets/6e55642b-41be-44d4-ab6e-7c4ab92baa5a
