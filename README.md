# 🖼️ GenAI Image Generation Website with Amazon Bedrock

This project demonstrates how to build a serverless, AI-powered image generation website using Amazon Bedrock, AWS Lambda, API Gateway, and a static frontend hosted on Amazon S3. It leverages the Amazon Titan Image Generator G1 v2 model to create high-quality images from text prompts.

---

## 🚀 Features

- Generate images from text prompts using Amazon Bedrock.
- Serverless architecture with AWS Lambda and API Gateway.
- Static frontend hosted on Amazon S3.
- Scalable and cost-effective solution.

---

## 🏗️ Architecture Overview

The application follows a fully serverless architecture on AWS:

- **Frontend (React)**: Hosted on Amazon S3 with static website hosting.
- **API Gateway**: Serves as the entry point for frontend requests.
- **AWS Lambda**: Processes input and integrates with Amazon Bedrock.
- **Amazon Bedrock**: Powers image generation using Titan Image Generator G1 v2.
- **Amazon S3**: Stores and delivers static assets.

### 📌 Architecture Diagram

![Final Architecture](Final%20Architecture.png)

---

## 🧰 Project Setup

To get started with this project, you'll need to:

1. Clone the repository and install dependencies for both frontend and backend.
2. Deploy the backend using AWS SAM or Serverless Framework.
3. Configure your API endpoint in the frontend app.
4. Build the frontend and upload it to an S3 bucket with static website hosting enabled.
5. Open your website via the S3 public URL and start generating images!

For detailed steps, refer to the blog post:  
📖 [Build Your Own Image Generation Website with Amazon Bedrock](https://dev.to/sarvar_04)

---

## 🧠 Powered by Amazon Nova

This Website uses **Amazon Nova**, a powerful foundation model that enables:

- Text-to-image conversion
- Text summerization
- Text to video creation 

---

## 🤝 Connect with Me

If you run into any issues or have questions, feel free to reach out — just drop a comment or DM me. I’m always happy to help! 🙌

- 🔗 [Dev.to Profile](https://dev.to/sarvar_04)  
- 💼 [LinkedIn](https://www.linkedin.com/in/sarvar04/)

Let’s build something amazing together! 🚀

---

## 📄 License

This project is licensed under the MIT-0 License. See the [LICENSE](LICENSE) file for full details.

---

## 🙏 Special Thanks

- [Sarvar Nadaf](https://dev.to/sarvar_04) — for authoring the original tutorial and making AWS magic accessible!
- AWS Community Builders Program - empowering cloud builders worldwide.
