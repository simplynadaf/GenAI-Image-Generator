import json
import boto3
import base64
from datetime import datetime

s3 = boto3.client("s3")
BUCKET_NAME = "your-s3-bucket-name"  # Replace with your S3 bucket name

def lambda_handler(event, context):
    # Store the input data (prompt)
    input_prompt = event.get('prompt', 'The cat on beach')
    print(f"Input Prompt: {input_prompt}")

    bedrock_rtime = boto3.client("bedrock-runtime", region_name="us-east-1")

    kwargs = {
        "modelId": "amazon.nova-canvas-v1:0",
        "contentType": "application/json",
        "accept": "application/json",
        "body": json.dumps({
            "textToImageParams": {"text": input_prompt},
            "taskType": "TEXT_IMAGE",
            "imageGenerationConfig": {
                "cfgScale": 8,
                "seed": int(datetime.now().timestamp()) % 100000,
                "quality": "standard",
                "width": 1280,
                "height": 720,
                "numberOfImages": 1
            }
        })
    }

    response = bedrock_rtime.invoke_model(**kwargs)
    response_body = json.loads(response.get('body').read())

    # Extract the single image
    image_data = response_body["images"][0]
    image_bytes = base64.b64decode(image_data)

    # Generate a unique filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    sanitized_prompt = input_prompt.replace(" ", "_").replace(":", "").replace("/", "").replace("\\", "")[:50]  
    image_key = f"generated_images/{sanitized_prompt}_{timestamp}.png"

    # Upload to S3
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=image_key,
        Body=image_bytes,
        ContentType="image/png"
    )

    # Generate a pre-signed URL (valid for 1 hour)
    presigned_url = s3.generate_presigned_url(
        "get_object",
        Params={"Bucket": BUCKET_NAME, "Key": image_key},
        ExpiresIn=3600
    )

    return {
        "statusCode": 200,
        "body": json.dumps(presigned_url)
    }