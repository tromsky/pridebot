import requests
import os
from datetime import datetime

def main():

    # build header with bearer token
    bearer_token = os.environ.get('BEARER_TOKEN')
    auth_headers = {"Authorization": "Bearer {}".format(bearer_token)}

    username = "exxonmobil"

    # get the URL for the user's profile pic
    user = requests.get(f"https://api.twitter.com/2/users/by/username/{username}?user.fields=profile_image_url", headers=auth_headers)
    profile_pic = requests.get(user.json()["data"]["profile_image_url"])
    profile_pic_path = f"profile_pics/{username}_pp_{datetime.utcnow().isoformat()}.png"

    # write the profile pic
    with open(profile_pic_path, "wb") as f:
        f.write(profile_pic.content) 

if __name__ == "__main__":
    main()