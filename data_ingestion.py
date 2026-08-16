#To read and process the NAV data from xlsx.

import pandas as pd 

def load_data(filename: str):
    if not filename.endswith((".csv", ".xlsx")):
        raise ValueError("Filename must be an Excel or a CSV file")
    if filename .endswith(".csv"):
        df = pd.read_csv(filename)
    elif filename.endswith(".xlsx"):
        df = pd.read_excel(filename)

    required_columns = ["Fund Name", "Date", "NAV"]

    if list(df.columns) != required_columns:
        raise ValueError(f"Expected columns: {required_columns}, Found: {list(df.columns)}")
        
    df["Date"] = pd.to_datetime(df["Date"])
    df["NAV"] = pd.to_numeric(df["NAV"])

    return df 