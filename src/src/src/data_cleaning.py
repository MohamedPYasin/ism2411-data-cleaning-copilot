# The purpose of this code is to clean a messy dataset

import pandas as pd

def load_data(file_path): #Load data from the CSV file
    return pd.read_csv(file_path)

# Standardizing column names; converting to lowercase and replacing spaces with underscores
def standardize_column_names(df):  
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    return df
# Stripping leading/trailing whitespace for aesthetic consistency and ensuring accurate data.
def strip_whitespace(df):  
    text_columns = df.select_dtypes(include=["object"]).columns
    for col in text_columns:
        df[col] = df[col].astype(str).str.strip()
    return df
# Converting to numerics; coercing errors to NaN
def convert_to_numerics(df):  
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["qty"] = pd.to_numeric(df["qty"], errors="coerce")
    return df
# Drop missing prices and quantities
def handle_missing_values(df):  
    return df.dropna(subset=["price", "qty"]) 
# Remove data entry errors; negative prices and quantities
def remove_data_entry_errors(df):
    return df[(df["price"] >= 0) & (df["qty"] >= 0)]

if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    df_raw = load_data(raw_path)
    df_clean = standardize_column_names(df_raw)
    df_clean = strip_whitespace(df_clean)
    df_clean = convert_to_numerics(df_clean)
    df_clean = handle_missing_values(df_clean)
    df_clean = remove_data_entry_errors(df_clean)
    df_clean.to_csv(cleaned_path, index=False)
    print("Cleaning complete. First few rows:")
    print(df_clean.head())