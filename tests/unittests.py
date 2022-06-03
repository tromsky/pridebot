import unittest

from main import RAINBOW_BOUNDARIES, check_image_contains_colours


class TestSuite(unittest.TestCase):
    """
    Test suite
    """

    def test_rainbow_check(self):
        """
        Checks for known images for rainbows

        Facebook and RogersHelps contain raindows
        exxonmobil and fbsecurity do not contain rainbows
        """

        exxonmobil = "tests/profile_pics/exxonmobil_pp.png"
        facebook = "tests/profile_pics/Facebook_pp.png"
        rogers_helps = "tests/profile_pics/RogersHelps_pp.png"
        fb_security = "tests/profile_pics/fbsecurity_pp.png"

        self.assertFalse(check_image_contains_colours(exxonmobil, RAINBOW_BOUNDARIES))
        self.assertTrue(check_image_contains_colours(facebook, RAINBOW_BOUNDARIES))
        self.assertTrue(check_image_contains_colours(rogers_helps, RAINBOW_BOUNDARIES))
        self.assertFalse(check_image_contains_colours(fb_security, RAINBOW_BOUNDARIES))


if __name__ == "__main__":
    unittest.main()
