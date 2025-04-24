# 🖼️ GenAI Image Generation Website with Amazon Bedrock

This project demonstrates how to build a serverless, AI-powered image generation website using Amazon Bedrock, AWS Lambda, API Gateway, and a static frontend hosted on Amazon S3. It leverages the Amazon Titan Image Generator G1 v2 model to create high-quality images from text prompts.

## 🚀 Features

- Generate images from text prompts using Amazon Bedrock.
- Serverless architecture with AWS Lambda and API Gateway.
- Static frontend hosted on Amazon S3.
- Scalable and cost-effective solution.

## 🏗️ Architecture Overview

The application follows a serverless architecture on AWS:

- **Frontend (React)**: Hosted on Amazon S3 with static website hosting enabled.
- **API Gateway**: Receives HTTP requests from the frontend.
- **AWS Lambda**: Handles requests from the API Gateway and invokes Amazon Bedrock.
- **Amazon Bedrock**: Uses the Titan Image Generator G1 v2 model to generate images based on text prompts.
- **Amazon S3**: Also used to store or serve generated content (optional, if implementing image persistence).

### 📌 Architecture Diagram

![Final Architecture](Final%20Architecture.png)

## 📚 Prerequisites

- AWS account with access to Amazon Bedrock.
- AWS CLI configured with appropriate permissions.
- Node.js and npm installed.
- Basic knowledge of AWS services.

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/genai-image-generator.git
cd genai-image-generator
