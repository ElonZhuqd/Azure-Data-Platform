# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE SCHEMA IF NOT EXISTS audit;
# MAGIC
# MAGIC CREATE TABLE IF NOT EXISTS audit.load_logs (
# MAGIC     data_source STRING,
# MAGIC     tablename STRING,
# MAGIC     numberofrowscopied INT,
# MAGIC     watermarkcolumnname STRING,
# MAGIC     loaddate TIMESTAMP
# MAGIC );
# MAGIC
# MAGIC select * from audit.load_logs;

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC truncate table audit.load_logs
