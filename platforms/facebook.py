from dotenv import load_dotenv
import requests
import os
import json

load_dotenv()
PAGE_ID = os.getenv("FB_PAGE_ID")
ACCESS_TOKEN = os.getenv("FB_ACCESS_TOKEN")
# Your app credentials
APP_ID = os.getenv("APP_ID")
APP_SECRET = os.getenv("APP_SECRET")

def get_permanent_page_token():
    # 1. Extend user token to 60 days
    extend_url = f"https://graph.facebook.com/v19.0/oauth/access_token?grant_type=fb_exchange_token&client_id={APP_ID}&client_secret={APP_SECRET}&fb_exchange_token={ACCESS_TOKEN}"
    long_lived_token = requests.get(extend_url).json()['access_token']
    
    # 2. Get permanent page token
    accounts_url = f"https://graph.facebook.com/v19.0/me/accounts?access_token={long_lived_token}"
    accounts = requests.get(accounts_url).json()
    
    for page in accounts['data']:
        if page['id'] == PAGE_ID:
            return page['access_token']
    
    raise Exception("Page token not found")

def post_to_facebook(caption,image_url=None, media_type='text'):
    
    try:  
        if media_type == 'photo'and image_url:
            print(PAGE_ID,ACCESS_TOKEN)
            print("----------------------------------------")
        # Step 1: Upload the image to Facebook without publishing
            url = f'https://graph.facebook.com/v19.0/{PAGE_ID}/photos'
            payload ={
                'url' : image_url,
                'published' : False,
                'access_token' :ACCESS_TOKEN
            }
            upload_response = requests.post(url, data=payload)
            upload_data = upload_response.json()
            print(upload_data)
            if "id" not in upload_data:
                print("❌ Image upload failed:", upload_data)
                return upload_data

                # Step 2: Post the image with a caption using the uploaded media ID
            media_id = upload_data["id"]
            url = f'https://graph.facebook.com/v19.0/{PAGE_ID}/feed'
            payload = {
                "message": caption,
                "attached_media": json.dumps([{"media_fbid": str(media_id)}]),
                "published": True,
                "access_token": ACCESS_TOKEN
            }
            headers = {"Content-Type": "application/x-www-form-urlencoded"
    }
            try:
                response = requests.post(url,data=payload,headers=headers)
            except Exception as e:
                print(f"_________",str(e))
                return {"error": str(e)}
        print(response.status_code)
        print(response.json())
        return response.json()
    except Exception as e:
        print("❌ Exception occurred while posting to Facebook:", str(e))
        return {"error": str(e)}
         
    
    
   