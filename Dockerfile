FROM public.ecr.aws/lambda/python:3.9

# Install system dependencies required for pyarrow
RUN yum install -y gcc gcc-c++ python3-devel

# Copy requirements file
COPY requirements.txt ${LAMBDA_TASK_ROOT}

# Set environment variables to ensure proper numpy compilation
ENV OPENBLAS_NUM_THREADS=1
ENV NUMPY_EXPERIMENTAL_ARRAY_FUNCTION=0

# Install Python dependencies
RUN pip install --no-cache-dir numpy==1.24.3 && \
    pip install --no-cache-dir -r requirements.txt

# Copy function code
COPY src/ ${LAMBDA_TASK_ROOT}/

# Set the CMD to your handler
CMD ["app.lambda_handler"]