import pandas as pd
import os
import sqlalchemy

Connection = "postgresql+psycopg2://repl:password@localhost:5432/sales"
Query = "SELECT * FROM grocery_sales"

db_engine = sqlalchemy.create_engine(Connection)
grocery_sales = pd.read_sql(Query, db_engine)

# Extract function is already implemented for you 
def extract(store_data, extra_data):
    extra_df = pd.read_parquet(extra_data)
    merged_df = store_data.merge(extra_df, on = "index")
    return merged_df

