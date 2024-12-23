FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# Copy only the requirements.txt first to allow caching the pip install step
COPY requirements.txt requirements.txt

# Install the Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Now copy the rest of your application (after dependencies are installed)
COPY .streamlit .streamlit
COPY LICENSE LICENSE
COPY static static
COPY .env .env
COPY run_streamlit.py run_streamlit.py
COPY src src

# Expose the Streamlit port
EXPOSE 8501

# Define the basic ENTRYPOINT, without specific arguments
ENTRYPOINT ["streamlit", "run", "run_streamlit.py"]

# Optionally, we can define a default CMD as fallback for flexibility
CMD ["--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true"]


HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health


# ENTRYPOINT ["streamlit", "run", "run_streamlit.py", "--server.port=8501", "--server.address=0.0.0.0 --server.headless=true"]

#!/bin/bash

# source venv/bin/activate

# args="--server.address 0.0.0.0 --server.headless true"

# streamlit run $args run_streamlit.py
