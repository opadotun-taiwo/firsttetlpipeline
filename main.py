from extract import extract, grocery_sales
from transform import transform, avg_weekly_sales_per_month
from load import load, validation

if __name__ == "__main__":
    # Extract data
    merged_df = extract(grocery_sales, "extra_data.parquet")
    
    # Transform data
    clean_data = transform(merged_df)

    # Call the avg_weekly_sales_per_month() function and pass the cleaned DataFrame
    agg_data = avg_weekly_sales_per_month(clean_data)
    
    # Load data
    load(clean_data, "clean_data.csv", agg_data, "agg_data.csv")

    #validation
    validation("clean_data.csv")
    validation("agg_data.csv")
