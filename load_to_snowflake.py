import pandas as pd
import snowflake.connector

# ==========================================
# READ PARQUET FILE
# ==========================================

df = pd.read_parquet(
    r"C:\Users\DELL\Desktop\sales_data.parquet"
)

print("PARQUET FILE READ SUCCESSFULLY")
print(df.head())

# ==========================================
# CONNECT TO SNOWFLAKE
# ==========================================

conn = snowflake.connector.connect(
    user='prithiv',
    password='fdbrbr"gb,?E',
    account='bebrberb',
    warehouse='my_wh',
    database='retail_db',
    schema='retail_schema'
)

cursor = conn.cursor()

# ==========================================
# INSERT DATA INTO SNOWFLAKE
# ==========================================

for index, row in df.iterrows():

    insert_query = f"""
    INSERT INTO sales_data VALUES (
        '{row[0]}',
        '{row[1]}',
        '{row[2]}',
        '{row[3]}',
        '{row[4]}',
        '{row[5]}',
        '{row[6]}',
        '{row[7]}',
        '{row[8]}',
        '{row[9]}',
        '{row[10]}',
        '{row[11]}',
        '{row[12]}',
        '{row[13]}',
        '{row[14]}',
        '{row[15]}',
        '{row[16]}',
        '{row[17]}',
        '{row[18]}',
        '{row[19]}',
        '{row[20]}'
    )
    """

    cursor.execute(insert_query)

print("DATA LOADED INTO SNOWFLAKE SUCCESSFULLY")

cursor.close()
conn.close()