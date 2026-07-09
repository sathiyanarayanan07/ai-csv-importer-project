import pandas as pd

def read_csv(file_path):

    df = pd.read_csv(file_path)

    df = df.fillna("")

    return {
        "columns": list(df.columns),
        "total_rows": len(df),
        "preview": df.head(10).to_dict(orient="records"),
        "records": df.to_dict(orient="records")
    }