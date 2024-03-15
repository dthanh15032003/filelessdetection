# Fileless Malware Detection Tool

This repository contains code for a Fileless Malware Detection Tool designed to analyze files and system memory for potential fileless malware using AWS Lambda functions, EC2 instances, and machine learning models. 

## Lambda Functions

### lambda1 (s3ToEC2)

- **Purpose**: Triggered by S3 events, this Lambda function copies uploaded files from an S3 bucket to an EC2 instance using AWS Systems Manager (SSM).
- **Functionality**:
  - Retrieves S3 bucket name and object key from the event.
  - Copies the file to the specified EC2 instance.
  - Executes commands on the EC2 instance to analyze the file.
- **Dependencies**: boto3, urllib.parse

### lambda2 (bash)

- **Purpose**: Another Lambda function for copying files to an EC2 instance and executing a bash script for analysis.
- **Functionality**:
  - Retrieves S3 bucket name and object key from the event.
  - Copies the file to the specified EC2 instance.
  - Executes a bash script (`bashscript.sh`) on the EC2 instance for analysis.
- **Dependencies**: boto3, urllib.parse

### lambda3 (predict)

- **Purpose**: Lambda function for executing Python script `predict.py` on an EC2 instance to perform predictions.
- **Functionality**:
  - Executes a Python script (`predict.py`) on the EC2 instance to perform predictions.
  - Saves the prediction results to a file (`r.txt`).
  - Copies the result file to an S3 bucket.
- **Dependencies**: boto3

### lambda4 (sendfinal)

- **Purpose**: Lambda function for sending final analysis results.
- **Functionality**:
  - Sends the final analysis results to an S3 bucket.
- **Dependencies**: None

## EC2 Instance

- **Purpose**: The EC2 instance serves as the computing environment for executing file analysis scripts.
- **Functionality**:
  - Receives files from S3 for analysis.
  - Executes bash scripts and Python scripts for malware detection and prediction.
  - Sends analysis results back to S3.

## Frontend

### frontend.py

- **Purpose**: PyQt5-based GUI application for uploading files and monitoring the analysis process.
- **Functionality**:
  - Allows users to upload files for analysis.
  - Provides visual feedback on the analysis progress.
  - Displays analysis results to the user.
- **Dependencies**: PyQt5

## Machine Learning Model

- **File**: `model.pkl`
- **Purpose**: A trained machine learning model used for malware detection and prediction.
- **Functionality**: Predicts whether a file contains malware or is benign based on extracted features.

## Other Files

- **`bashscript.sh`**: Bash script for analyzing files using Volatility.
- **`predict.py`**: Python script for making predictions using the machine learning model.

## Usage

1. Ensure proper configuration of AWS IAM roles, S3 bucket, EC2 instance, and Lambda functions.
2. Upload files to the configured S3 bucket.
3. Lambda functions will automatically trigger file analysis on the EC2 instance.
4. Use the frontend application to monitor the analysis progress and view results.
5. Results will be stored in the S3 bucket.

## Memory Samples

- [Memory Sample 1](https://drive.google.com/file/d/148Xx4mrBbEpbbeC3Uk3Zi0R0xcDrMQg_/view?usp=sharing)
- [Memory Sample 2](https://drive.google.com/file/d/1CzTifXOpjYq4l3za7tStuvfU45EDwk6y/view?usp=sharing)
- [Memory Sample 3](https://drive.google.com/file/d/1rnCSRI9ORWoieZLcTKydTjxEW_H5gHpT/view?usp=sharing)
