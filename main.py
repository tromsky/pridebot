import os
from datetime import datetime

import cv2
import requests
import tweepy


def main():
    username = "exxonmobil"
    bearer_token = os.environ.get("BEARER_TOKEN")
    client = tweepy.Client(bearer_token)

    user = client.get_user(username=username, user_fields="profile_image_url")
    profile_pic = requests.get(user[0].data["profile_image_url"])
    profile_pic_path = f"profile_pics/{username}_pp_{datetime.utcnow().isoformat()}.png"

    # write the profile pic
    with open(profile_pic_path, "wb") as f:
        f.write(profile_pic.content)


if __name__ == "__main__":
    main()
