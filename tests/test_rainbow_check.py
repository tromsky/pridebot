import unittest

from main import check_image_contains_raindow

exxonmobil = "tests/profile_pics/exxonmobil_pp.png"
facebook = "tests/profile_pics/Facebook_pp.png"
rogers_helps = "tests/profile_pics/RogersHelps_pp.png"
fb_security = "tests/profile_pics/fbsecurity_pp.png"


class TestRainbowCheck(unittest.TestCase):
    """
    Test suite for image rainbow check
    """

    def test_check(self):
        """
        Checks for known images for rainbows
        """

        self.assertFalse(check_image_contains_raindow(exxonmobil))
        self.assertFalse(check_image_contains_raindow(exxonmobil))
        self.assertFalse(check_image_contains_raindow(exxonmobil))
        self.assertFalse(check_image_contains_raindow(exxonmobil))


if __name__ == "__main__":
    unittest.main()
