import pandas as pd
from sqlalchemy import create_engine

# CSV file path
file_path = r"C:\Users\DELL\Downloads\archive\Sales_data.csv"

# Read CSV
df = pd.read_csv(file_path)

# MySQL connection
engine = create_engine(
    "mysql+pymysql://root:123456789@localhost:3306/retail_db"
)

# Upload dataframe to MySQL
df.to_sql(
    name='sales_data',
    con=engine,
    if_exists='replace',
    index=False
)

print("CSV imported successfully!")