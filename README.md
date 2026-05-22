# End-to-End Data Engineering Pipeline

## Project Overview

Built an end-to-end cloud ETL pipeline using:

- MySQL
- Python
- AWS S3
- Parquet
- Snowflake

## Architecture

Kaggle CSV
→ MySQL
→ Python ETL
→ AWS S3/raw
→ Parquet Transformation
→ AWS S3/target
→ Snowflake

## Technologies Used

- Python
- Pandas
- boto3
- SQLAlchemy
- PyArrow
- Snowflake Connector
- AWS S3
- MySQL
- Snowflake

## Pipeline Steps

1. Load Kaggle CSV into MySQL
2. Extract MySQL table using Python
3. Upload raw CSV to S3
4. Convert CSV to Parquet
5. Upload Parquet to S3
6. Load data into Snowflake

## Author

Prithiv Nagarajan 