import pandas as pd

# Read the CSV files
df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_2.csv")

# Filter rows by product type (keeping only Pink Morsels)
df1 = df1[df1["product"] == "pink morsel"]
df2 = df2[df2["product"] == "pink morsel"]
df3 = df3[df3["product"] == "pink morsel"]
df1["price"] = df1["price"].str.replace("$", "").astype(float)
df2["price"] = df2["price"].str.replace("$", "").astype(float)
df3["price"] = df3["price"].str.replace("$", "").astype(float)


# Combine quantity and price into sales
df1["sales"] = df1["quantity"] * df1["price"]
df2["sales"] = df2["quantity"] * df2["price"]
df3["sales"] = df3["quantity"] * df3["price"]

# Select and rearrange fields for the output
output_df1 = df1[["sales", "date", "region"]]
output_df2 = df2[["sales", "date", "region"]]
output_df3 = df3[["sales", "date", "region"]]

# Concatenate the DataFrames vertically
merged_df = pd.concat([output_df1, output_df2, output_df3], ignore_index=True)

# Save the output to a CSV file
merged_df.to_csv("formatted_output.csv", index=False)