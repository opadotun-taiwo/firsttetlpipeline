import pandas as pd
import os

def transform(raw_data):
    raw_data.fillna(
      {
          'CPI': raw_data['CPI'].mean(),
          'Weekly_Sales': raw_data['Weekly_Sales'].mean(),
          'Unemployment': raw_data['Unemployment'].mean(),
      }, inplace = True
    )
    
    raw_data["Month"] = raw_data["Date"].dt.month
    raw_data = raw_data.loc[raw_data["Weekly_Sales"] > 10000, :]
    
    raw_data = raw_data.drop(["index", "Temperature", "Fuel_Price", "MarkDown1",    
                              "MarkDown2", "MarkDown3", "MarkDown4", "MarkDown5", "Type", 
                              "Size", "Date"], axis = 1)
    
    clean_data = transform(merged_df)
    

def avg_weekly_sales_per_month(clean_data):
  	# Select the "Month" and "Weekly_Sales" columns as they are the only ones needed for this analysis
    holidays_sales = clean_data[["Month", "Weekly_Sales"]]
   	# Create a chain operation with groupby(), agg(), reset_index(), and round() functions
    # Group by the "Month" column and calculate the average monthly sales
    # Call reset_index() to start a new index order
    # Round the results to two decimal places
    
    holidays_sales = (holidays_sales.groupby("Month")
    .agg(Avg_Sales = ("Weekly_Sales", "mean"))
    .reset_index().round(2))
    return holidays_sales

# Call the avg_weekly_sales_per_month() function and pass the cleaned DataFrame
agg_data = avg_weekly_sales_per_month(clean_data)