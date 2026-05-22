import pandas as pd
import boto3

# ==========================================
# AWS CONFIG
# ==========================================

aws_access_key = "AKIAdb26sarberbereJUYBKZ"
aws_secret_key = "t5yjrgrrJttd+frbarr/xg9xt8Lpum"

bucket_name = "prithiv-data-engineering-project"

s3 = boto3.client(
    "s3",
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name="ap-south-1"
)

# ==========================================
# READ LOCAL CSV
# ==========================================

df = pd.read_csv(r"C:\Users\DELL\Downloads\archive\sales_data.csv")

print("CSV READ SUCCESSFULLY")
print(df.head())

# ==========================================
# CONVERT TO PARQUET
# ==========================================

parquet_file = "sales_data.parquet"

df.to_parquet(
    parquet_file,
    index=False,
    engine="pyarrow"
)

print("PARQUET FILE CREATED")

# ==========================================
# UPLOAD PARQUET TO S3
# ==========================================

s3.upload_file(
    parquet_file,
    bucket_name,
    "target/sales_data.parquet"
)

print("PARQUET FILE UPLOADED TO S3")