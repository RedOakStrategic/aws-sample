import os
import boto3
import pandas as pd

def lambda_handler(event, context):
    """
    Lambda function that processes CSV files from the raw bucket and converts them to parquet
    in the processed bucket.
    """
    # Get bucket names from environment variables
    raw_bucket = os.environ['RAW_BUCKET']
    processed_bucket = os.environ['PROCESSED_BUCKET']
    
    # Get the S3 client
    s3_client = boto3.client('s3')
    
    try:
        # Get the source file details from the event
        source_key = event['detail']['object']['key']
        
        # Download the CSV file
        response = s3_client.get_object(Bucket=raw_bucket, Key=source_key)
        
        # Read the CSV into a pandas DataFrame
        df = pd.read_csv(response['Body'])
        
        # Print row count to CloudWatch logs
        row_count = len(df)
        print(f"Processing file {source_key} with {row_count} rows")
        
        # Handle NA values in sex column
        if 'sex' in df.columns:
            df['sex'] = df['sex'].fillna('Unknown')
            # Drop remaining NA values from all columns
            df = df.dropna()
            print(f"After NA handling, file has {len(df)} rows")
        
        # Generate the output key (replace .csv with .parquet)
        output_key = source_key.rsplit('.', 1)[0] + '.parquet'
        
        # Convert to parquet and save to memory
        parquet_buffer = df.to_parquet()
        
        # Upload to processed bucket
        s3_client.put_object(
            Bucket=processed_bucket,
            Key=output_key,
            Body=parquet_buffer
        )
        
        return {
            'statusCode': 200,
            'body': f'Successfully processed {source_key} with {row_count} rows'
        }
        
    except Exception as e:
        print(f"Error processing file: {str(e)}")
        raise