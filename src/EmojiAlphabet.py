class EmojiAlphabet:
    def __init__(self, emoji):
        self.emoji = emoji

    def a(self):
        emoji = self.emoji
        _s = "　"
        emoji_char = \
            ('{}{}{}\n'.format(_s, emoji, emoji)) + \
            ('{}{}{}\n'.format(emoji, _s, emoji)) + \
            ('{}{}{}\n'.format(emoji, emoji, emoji)) + \
            ('{}{}{}\n'.format(emoji, _s, emoji)) + \
            ('{}{}{}\n'.format(emoji, _s, emoji))
        return emoji_char

    def b(self):
        emoji = self.emoji
        _s = "　"
        emoji_char = \
            ('{}{}{}\n'.format(emoji, emoji, _s)) + \
            ('{}{}{}\n'.format(emoji, _s, emoji)) + \
            ('{}{}{}\n'.format(emoji, emoji, emoji)) + \
            ('{}{}{}\n'.format(emoji, _s, emoji)) + \
            ('{}{}{}\n'.format(emoji, emoji, _s))
        return 

    def c(self):
        emoji = self.emoji
        _s = "　"
        emoji_char = \
            ('{}{}{}\n'.format(_s, emoji, emoji)) + \
            ('{}{}{}\n'.format(emoji, _s, _s)) + \
            ('{}{}{}\n'.format(emoji, _s, _s)) + \
            ('{}{}{}\n'.format(emoji, _s, _s)) + \
            ('{}{}{}\n'.format(_s, emoji, emoji))
        return emoji_char

    def emoji_char(self, string):
        emoji_generator = {
            'a': self.a,
        }

        emoji_string = []

        for char in string:
            foo = emoji_generator.get(char, "No emoji for this char")
            emoji_string.append(foo())

        # it returns a var which had milti line prints in it.
        return emoji_string
