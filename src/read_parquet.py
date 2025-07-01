import boto3
import pandas as pd
from io import BytesIO

def read_s3_parquet():
    # Create a session using the ros-sandbox profile
    session = boto3.Session(profile_name='ros-sandbox')
    
    # Create an S3 client using the session
    s3_client = session.client('s3')
    
    # S3 bucket and key information
    bucket = '985803916100-proposal-processed'
    key = 'penguins.parquet'
    
    try:
        # Get the parquet file from S3
        response = s3_client.get_object(Bucket=bucket, Key=key)
        
        # Create a BytesIO object from the response body
        parquet_buffer = BytesIO(response['Body'].read())
        
        # Read the parquet file into a pandas DataFrame using the buffer
        df = pd.read_parquet(parquet_buffer)
        
        # Print the first few rows
        print("\nFirst few rows of the penguins dataset:")
        print(df.head())
        
        return df
        
    except Exception as e:
        print(f"Error reading parquet file: {str(e)}")
        raise

if __name__ == "__main__":
    read_s3_parquet()