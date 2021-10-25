import unittest

from core import translateMessageToBinary, translateBinaryToGithubReactions


class CoreTests(unittest.TestCase):
    def test_translateMessageToBinary(self):
        self.assertEqual(translateMessageToBinary(["rocket", "-1", "eyes"]), "01101000")
        self.assertEqual(
            translateMessageToBinary(["laugh", "rocket", "-1", "heart", "eyes", "+1", "hooray", "confused"]),
            "11111111")
        self.assertEqual(translateMessageToBinary([""]), "00000000")
        self.assertEqual(translateMessageToBinary(["laugh", "rocket", "-1", "eyes"]), "11101000")

    def test_translateBinaryToGithubReactions(self):
        self.assertEqual(translateBinaryToGithubReactions("01101000"), ["rocket", "-1", "eyes"])
        self.assertEqual(
            translateBinaryToGithubReactions("11111111"),
            ["laugh", "rocket", "-1", "heart", "eyes", "+1", "hooray", "confused"])
        self.assertEqual(translateBinaryToGithubReactions("00000000"), [])
        self.assertEqual(translateBinaryToGithubReactions("11101000"), ["laugh", "rocket", "-1", "eyes"])


if __name__ == '__main__':
    unittest.main()
