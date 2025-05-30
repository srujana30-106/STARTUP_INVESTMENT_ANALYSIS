import pandas as pd
import re

# File path
file_path = r"C:\Users\RGUKT\Desktop\STARTUP_INVESTMENTS\investments_VC.csv"

#Read CSV with encoding fallback
try:
    df = pd.read_csv(file_path, encoding='utf-8')
except UnicodeDecodeError:
    df = pd.read_csv(file_path, encoding='latin1')

#Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
df = df.dropna(subset=['name'])
df = df.drop_duplicates(subset=['permalink'])
df['name'] = df['name'].apply(lambda x: re.sub(r'[^A-Za-z\s]', '', str(x)))  # Remove numbers and special characters
df['name'] = df['name'].str.replace(r'\s+', ' ', regex=True).str.strip()     # Clean up extra spaces
df['name'] = df['permalink'].apply(lambda x: str(x).rstrip('/').split('/')[-1])

# Drop rows where 'name' is now empty
df.dropna(inplace=True)

# Extract name from permalink, then clean
df['name'] = df['permalink'].apply(lambda x: str(x).rstrip('/').split('/')[-1])
df['name'] = df['name'].str.replace(r'[^A-Za-z0-9\s]', '', regex=True).str.strip()

# Drop empty names
df = df[df['name'].str.len() > 0]
#Clean 'funding_total_usd' column
if 'funding_total_usd' in df.columns:
    df['funding_total_usd'] = (
        df['funding_total_usd']
        .astype(str)
        .str.replace(',', '', regex=False)
        .str.strip()
    )
    df['funding_total_usd'] = pd.to_numeric(df['funding_total_usd'], errors='coerce')

#Convert date columns
date_columns = ['founded_at', 'first_funding_at', 'last_funding_at']
for col in date_columns:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors='coerce', dayfirst=False)

#Basic stats
print(f"Total records: {len(df)}")
print(f"Operating companies: {len(df[df['status'] == 'operating'])}")
if 'market' in df.columns:
    print(f"Games market companies: {len(df[df['market'].str.lower() == 'games'])}")
else:
    print(" 'market' column not found.")

# List of numeric columns that should be integers
numeric_cols = [
    'funding_rounds', 'seed', 'venture', 'equity_crowdfunding', 'undisclosed',
    'convertible_note', 'debt_financing', 'angel', 'grant', 'private_equity',
    'post_ipo_equity', 'post_ipo_debt', 'secondary_market', 'product_crowdfunding',
    'round_A', 'round_B', 'round_C', 'round_D', 'round_E', 'round_F', 'round_G', 'round_H'
]

for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)
# Year and month columns to fix
year_cols = ['founded_year', 'founded_month']

for col in year_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)


# Save to a new file
output_path = r"C:\Users\RGUKT\Desktop\STARTUP_INVESTMENTS\investments_VC_cleaned.csv"
df.to_csv(output_path, index=False, encoding='utf-8-sig')
print("Cleaned dataset saved to:", output_path)



