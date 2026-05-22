import boto3
import pandas as pd
import snowflake.connector

# =====================================================
# AWS CONFIGURATION
# =====================================================

aws_access_key = "fearhrhre"
aws_secret_key = "t5yjJttd+fnzfhehdfdf/xg9xt8Lpum"

bucket_name = "prithiv-data-engineering-project"

# S3 parquet file location
s3_key = "target/sales_data.parquet"

# =====================================================
# DOWNLOAD PARQUET FILE FROM S3
# =====================================================

s3 = boto3.client(
    "s3",
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name="ap-south-1"
)

local_parquet_file = "sales_data.parquet"

s3.download_file(
    bucket_name,
    s3_key,
    local_parquet_file
)

print("PARQUET FILE DOWNLOADED FROM S3")

# =====================================================
# READ PARQUET FILE
# =====================================================

df = pd.read_parquet(local_parquet_file)

print("\nDATA PREVIEW:")
print(df.head())

print("\nCOLUMN NAMES:")
print(df.columns)

# =====================================================
# SNOWFLAKE CONNECTION
# =====================================================

conn = snowflake.connector.connect(
    user='prithiv',
    password='6yyjGk"hrrhrh,?E',
    account='sbbfbd.ap-southeast-5.aws',
    warehouse='my_wh',
    database='retail_db',
    schema='retail_schema'
)

cursor = conn.cursor()

print("\nCONNECTED TO SNOWFLAKE")

# =====================================================
# INSERT DATA INTO SNOWFLAKE
# =====================================================

for index, row in df.iterrows():

    values = []

    for value in row:
        value = str(value)

        # Handle single quotes safely
        value = value.replace("'", "''")

        values.append(value)

    values_string = "', '".join(values)

    insert_query = f"""
    INSERT INTO sales_data VALUES ('{values_string}')
    """

    cursor.execute(insert_query)

print("\nDATA LOADED INTO SNOWFLAKE SUCCESSFULLY")

# =====================================================
# CLOSE CONNECTION
# =====================================================

cursor.close()
conn.close()

print("\nSNOWFLAKE CONNECTION CLOSED")