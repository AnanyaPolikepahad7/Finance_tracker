# import pandas as pd

# def load_and_clean_data(filepath):
#     try:
#         df = pd.read_csv(filepath, header=0)
#     except Exception as e:
#         raise FileNotFoundError(f"Error reading file: {e}")

#     # Normalize column names (capitalize & strip spaces)
#     # df.columns = [col.strip().capitalize() for col in df.columns]
#     df.columns = df.columns.str.strip()  # Remove whitespace

#     # Parse dates with flexible formats
#     df['Date'] = pd.to_datetime(df['Date'], errors='coerce', dayfirst=True)

#     # Drop rows with invalid or missing dates or amounts
#     df.dropna(subset=['Date', 'Amount'], inplace=True)

#     # Fill missing categories with 'Uncategorized'
#     if 'Category' in df.columns:
#         df['Category'] = df['Category'].fillna('Uncategorized')

#     # Ensure amount is float
#     df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
#     df.dropna(subset=['Amount'], inplace=True)

#     # Clean whitespace in string columns
#     str_cols = df.select_dtypes(include='object').columns
#     for col in str_cols:
#         df[col] = df[col].astype(str).str.strip()

#     return df
import pandas as pd

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath)

    df['Date'] = pd.to_datetime(df['Date'], format="%Y-%m-%d", errors='coerce', dayfirst=False)
    df['Time'] = pd.to_datetime(df['Time'], format="%H:%M", errors='coerce').dt.strftime('%H:%M')
    df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
    df['Recurring'] = df['Recurring'].astype(str).str.lower().map({'true': True, 'false': False})

    df.dropna(subset=['Date', 'Time', 'Amount'], inplace=True)
    return df
