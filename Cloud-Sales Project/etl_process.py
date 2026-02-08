import boto3
import pandas as pd
import io
from datetime import datetime

# --- CONFIGURATION ---
ACCESS_KEY = 'YOUR_ACCESS_KEY_HERE'
SECRET_KEY = 'YOUR_SECRET_KEY_HERE'
REGION = 'ap-south-1'
BUCKET_NAME = 'sales-data-project-unique-id'
RAW_FILE_KEY = 'raw-data/sales_data_sample.csv'
# This creates a unique filename every time you run it
PROCESSED_FILE_KEY = f'processed-data/cleaned_sales_{datetime.now().strftime("%Y%m%d_%H%M")}.csv'

def run_etl():
    try:
        # 1. CONNECT TO S3
        s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY, region_name=REGION)
        print("✅ Connected to AWS S3")

        # 2. EXTRACT
        obj = s3.get_object(Bucket=BUCKET_NAME, Key=RAW_FILE_KEY)
        df = pd.read_csv(io.BytesIO(obj['Body'].read()), encoding='unicode_escape')
        print(f"✅ Extracted {len(df)} rows")

        # 3. TRANSFORM (Cleaning)
        # Convert date and handle errors
        df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])
        
        # Select only the important columns for the dashboard to keep it clean
        columns_to_keep = [
            'ORDERNUMBER', 'QUANTITYORDERED', 'PRICEEACH', 
            'SALES', 'ORDERDATE', 'STATUS', 'PRODUCTLINE', 
            'CUSTOMERNAME', 'CITY', 'COUNTRY'
        ]
        df_cleaned = df[columns_to_keep].copy()

        # Remove any rows with missing critical data
        df_cleaned = df_cleaned.dropna()
        
        print("✅ Data Cleaned & Columns Filtered")

        # 4. LOAD (Upload back to S3)
        csv_buffer = io.StringIO()
        df_cleaned.to_csv(csv_buffer, index=False)
        
        s3.put_object(
            Bucket=BUCKET_NAME, 
            Key=PROCESSED_FILE_KEY, 
            Body=csv_buffer.getvalue()
        )
        print(f"🚀 SUCCESS: Processed file uploaded to: {PROCESSED_FILE_KEY}")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    run_etl()