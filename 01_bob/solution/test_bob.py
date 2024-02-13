import unittest
import bob


class TestReply(unittest.TestCase):
    def test_question(self):
        self.assertEqual(bob.reply("How are you?"), "Sure")
        self.assertEqual(bob.reply("Hi? "), "Sure")

    def test_yell(self):
        self.assertEqual(bob.reply("HEY"), "Whoa, chill out!")

    def test_question_yell(self):
        self.assertEqual(bob.reply("DUDE?"), "Calm down, I know what I'm doing!")

    def test_silence(self):
        self.assertEqual(bob.reply(""), "Fine. Be that way!")
        self.assertEqual(bob.reply("  "), "Fine. Be that way!")
        self.assertEqual(bob.reply(" \n"), "Fine. Be that way!")

    def test_else(self):
        self.assertEqual(bob.reply("asdkoqwmem"), "Whatever.")
