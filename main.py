import os
from datetime import datetime

import cv2
import numpy as np
import requests

COLOUR_BOUNDARIES = [
    ([175, 50, 20], [180, 255, 255]),  # red
    ([10, 50, 20], [25, 255, 255]),  # orange/brown
    ([28, 50, 20], [35, 255, 255]),  # yellow
    ([40, 50, 20], [75, 255, 255]),  # blue
    ([95, 50, 20], [125, 255, 255]),  # green
    ([120, 50, 20], [135, 255, 255]),  # violet/purple
]

USERNAMES = ["exxonmobil", "RogersHelps", "Facebook", "fbsecurity"]


def check_image_contains_raindow(image_path):
    """
    Given an image path, check to see if the image likely contains
    anything like a rainbow by checking for existance of ROYGBV
    pixels.

    returns a Bool, True is all colours are contained in the image
    """

    # set a control flag and load the image
    image_contains_rainbow = False
    image = cv2.imread(image_path)

    # loop over the colour boundaries
    for (lower, upper) in COLOUR_BOUNDARIES:

        # create NumPy arrays from the colour boundaries
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")

        # find the colors within the specified boundaries and apply
        # the mask
        img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(img_hsv, lower, upper)

        # check for perfect saturation in the mask
        image_contains_rainbow = 255 in mask

        # for debugging, hit "0" key to continue
        # output = cv2.bitwise_and(image, image, mask=mask)
        # cv2.imshow("images", np.hstack([image, output]))
        # cv2.waitKey(0)

    return image_contains_rainbow


def main():

    # build header with bearer token
    bearer_token = os.environ.get("BEARER_TOKEN")
    auth_headers = {"Authorization": f"Bearer {bearer_token}"}

    for username in USERNAMES:

        # get the URL for the user's profile pic
        user = requests.get(
            f"https://api.twitter.com/2/users/by/username/{username}?user.fields=profile_image_url",
            headers=auth_headers,
        )
        profile_pic = requests.get(user.json()["data"]["profile_image_url"])
        profile_pic_path = (
            f"profile_pics/{username}_pp_{datetime.utcnow().isoformat()}.png"
        )

        # write the profile pic
        with open(profile_pic_path, "wb") as f:
            f.write(profile_pic.content)

        print(
            f"{username}'s profile pic likely contains rainbow: {check_image_contains_raindow(profile_pic_path)}"
        )


if __name__ == "__main__":
    main()
