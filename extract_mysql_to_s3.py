import pandas as pd
from sqlalchemy import create_engine
import boto3

# ==========================================
# MYSQL CONNECTION
# ==========================================

# Replace with your MySQL password
mysql_password = "12342352354656789"

engine = create_engine(
    f"mysql+pymysql://root:{mysql_password}@localhost:3306/retail_db"
)

# ==========================================
# READ DATA FROM MYSQL
# ==========================================

query = "SELECT * FROM sales_data"

df = pd.read_sql(query, engine)

print("DATA FROM MYSQL:")
print(df.head())

# ==========================================
# SAVE CSV LOCALLY
# ==========================================

local_file = "sales_data.csv"

df.to_csv(local_file, index=False)

print("CSV SAVED LOCALLY")

# ==========================================
# AWS S3 CONNECTION
# ==========================================

# Replace with your AWS credentials
aws_access_key = "dnstnnrnsry"
aws_secret_key = "t5yjJttd+nttrntsnt/xg9xt8Lpum"

# Replace with your bucket name
bucket_name = "prithiv-data-engineering-project"

s3 = boto3.client(
    "s3",
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name="ap-south-1"
)

# ==========================================
# UPLOAD FILE TO S3
# ==========================================

s3.upload_file(
    local_file,
    bucket_name,
    "raw/sales_data.csv"
)

print("FILE UPLOADED TO S3 SUCCESSFULLY")