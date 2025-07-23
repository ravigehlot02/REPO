from dotenv import load_dotenv
import requests
import os


load_dotenv()
ACCESS_TOKEN = os.getenv("IG_ACCESS_TOKEN") # env variables
IG_USER_ID = os.getenv("IG_USER_ID")

def create_media_object(image_url, caption):
    endpoint = f"https://graph.facebook.com/v19.0/{IG_USER_ID}/media"
    payload = {
        "image_url": image_url,
        "caption": caption,
        "access_token": ACCESS_TOKEN
    }
    response = requests.post(endpoint, data=payload)
    result = response.json()
    print("🖼️ Media Creation Response:", result)
    return result.get("id")  # ✅ lowercase key

def publish_media(media_id):
    endpoint = f"https://graph.facebook.com/v19.0/{IG_USER_ID}/media_publish"
    payload = {
        "creation_id": media_id,
        "access_token": ACCESS_TOKEN
    }
    response = requests.post(endpoint, data=payload)
    print("🚀 Publish Response:", response.json())
    return response.json()

def post_image(image_url, caption):
    media_id = create_media_object(image_url, caption)
    if media_id:
        return publish_media(media_id)
    else:
        print("❌ Failed to create media object.")
