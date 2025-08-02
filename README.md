# 🗓️ Social Media Scheduler

A Python-based social media scheduler that automates posting to **Instagram** and **Facebook** based on a scheduled timeline defined in a JSON file.

---

## 🚀 Features

- ✅ Schedule posts with captions, images, and platforms (Facebook, Instagram)
- 📆 Check due posts every minute
- 📸 Automatically publish to Instagram and Facebook
- 🔁 Runs continuously as a background scheduler
- 💾 Saves updated post status (posted/unposted)

---

## 📂 Project Structure

```bash
scheduler/
├── scheduler.py               # Main scheduler loop
├── data/
│   └── schedule.json          # Post schedule and metadata
├── content_manager.py         # Loads schedule from file
├── platforms/
│   ├── facebook.py            # Facebook posting logic
│   └── instagram.py           # Instagram posting logic
└── classes/
    └── Schedule.py            # Schedule data class
````

---

## 📦 Requirements

* Python 3.9+
* Valid Facebook Graph API setup
* Valid Instagram Graph API setup

---

## 🔧 Setup & Usage

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Prepare your `schedule.json`

Located at: `data/schedule.json`

Example:

```json
{
  "post_1": {
    "time": "2025-08-01 14:30:00",
    "caption": "Check out our new product!",
    "image_url": "https://example.com/image.jpg",
    "platform": ["facebook", "instagram"],
    "media_type": "image",
    "posted": false
  }
}
```

### 3. Run the scheduler

```bash
python scheduler.py
```

The scheduler will:

* Load all scheduled posts
* Check every minute if it's time to post
* Publish posts and update their status

---

## ⚙️ Functions Explained

### `schedule_runner(post_id=None)`

Scans all posts or a specific post by ID and publishes if it's due.

### `should_post(post_time)`

Checks if a scheduled post time is in the past.

### `save_schedule(schedule_map)`

Saves updated post statuses back to the schedule file.

---

## 🛠️ TODO (Future Improvements)

* Add dashboard UI to manage posts
* Add error logging and retry mechanism
* OAuth-based token management
* Support for Threads, Twitter (X), LinkedIn, etc.

---

## 👨‍💻 Author

Built by RaviG — Python developer automating digital workflows for content creators.

---

