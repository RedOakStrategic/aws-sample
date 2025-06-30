# AWS Serverless ETL Sample

This project demonstrates a serverless ETL process using AWS services. It automatically processes CSV files uploaded to an S3 bucket by converting them to Parquet format.

## Architecture

- AWS S3 buckets for raw (sample-raw) and processed (sample-processed) data
- AWS Lambda function for data processing
- Amazon EventBridge for event-driven processing
- AWS SAM for infrastructure as code
- Docker container with Python 3.9 and pyarrow

## Prerequisites

- AWS SAM CLI
- Docker
- AWS CLI configured with appropriate credentials
- GitHub repository with appropriate AWS credentials configured as secrets:
  - AWS_ACCESS_KEY_ID
  - AWS_SECRET_ACCESS_KEY

## Deployment

### Manual Deployment

1. Build the application:
```bash
sam build
```

2. Deploy the application:
```bash
sam deploy --guided
```

### Automated Deployment

The project includes a GitHub Actions workflow that automatically builds and deploys the application when changes are pushed to the main branch. The workflow:

1. Sets up Python and AWS SAM
2. Configures AWS credentials
3. Builds the application using SAM
4. Deploys to AWS using SAM

To use the automated deployment:

1. Fork this repository
2. Configure AWS credentials as GitHub repository secrets:
   - AWS_ACCESS_KEY_ID
   - AWS_SECRET_ACCESS_KEY
3. Push changes to the main branch to trigger the deployment

## Usage

1. Upload a CSV file to the `sample-raw` bucket
2. The Lambda function will automatically:
   - Process the file
   - Print the row count to CloudWatch logs
   - Save the file as Parquet in the `sample-processed` bucket

## Project Structure

- `template.yaml`: SAM template defining AWS resources
- `src/app.py`: Lambda function code
- `Dockerfile`: Container configuration for Lambda
- `requirements.txt`: Python dependencies