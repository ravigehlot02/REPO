from content_manager import load_schedule    
from platforms.facebook import post_to_facebook
from platforms.instagram import create_media_object,publish_media
from datetime import datetime
from classes.Schedule import Schedule
from typing import Dict
import json
import time

schedule_map: Dict[str, Schedule] ={}
SCHEDULE_FILE = "data/schedule.json"
TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
def schedule_runner(post_id = None):
    """
    Runs the scheduler. If post_id is provided, only attempts to post that ID.
    Otherwise, scans all scheduled posts and posts any that are due.
    """
    schedule_map = load_schedule()
    updated = False
    schedule = Schedule
    # Decide what to process
    posts_to_check = {post_id: schedule_map[post_id]} if post_id else schedule_map

    for key,schedule in posts_to_check.items():
        if schedule.posted == False and should_post(schedule.time):
            if "instagram" in schedule.platform:
                print(f"📸 IG Posting: {schedule.caption}")
                media_id = create_media_object(schedule.image_url, schedule.caption)
                if media_id:
                    publish_media(media_id)
                    print("✅ Instagram post successful.")
                else:
                    print("❌ Instagram media creation failed.")
            if "facebook" in schedule.platform:
                print(f"📸 FB Posting: {schedule.caption}")
                fb_response = post_to_facebook(schedule.caption,
                                        str(schedule.image_url),schedule.media_type)
                if fb_response and "id" in fb_response:
                    print("✅ Facebook post successful.")
                    schedule.posted = True
                    updated = True
                else:
                    print("❌ Facebook post failed:", fb_response)   
        if updated:
            schedule_map[key]= schedule
            save_schedule(schedule_map)
            print("📝 Schedule updated.")

    
    return schedule_map

def should_post(post_time):
    """Check whether the post time is in the past (i.e., it's time to post).
    """
    now = datetime.now()
    return now >= post_time


def save_schedule(schedule_map):
    """
    Save the updated schedule back to the JSON file.
    """
    with open(SCHEDULE_FILE, "w", encoding="utf-8") as f:
        json.dump(
            {
                key:schedule.model_dump(mode="json") 
                for key, schedule in schedule_map.items()
            },f,indent=4
        )

if __name__ == "__main__" :
    while True:
        schedule_runner()
        time.sleep(60)