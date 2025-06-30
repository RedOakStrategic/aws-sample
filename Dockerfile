FROM public.ecr.aws/lambda/python:3.9

# Install system dependencies required for pyarrow
RUN yum install -y gcc gcc-c++ python3-devel

# Copy requirements file
COPY requirements.txt ${LAMBDA_TASK_ROOT}

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy function code
COPY src/ ${LAMBDA_TASK_ROOT}/

# Set the CMD to your handler
CMD ["app.lambda_handler"]