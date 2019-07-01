class EmojiAlphabet:
    space = "　  "

    def __init__(self, emoji):
        self.emoji = emoji

    def a(self):
        E = self.emoji
        o = self.space
        return [
            '{}{}{}{}{}'.format(o, E, E, E, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, E, E, E, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
        ]

    def b(self):
        E = self.emoji
        o = self.space
        return [
            '{}{}{}{}{}'.format(E, E, E, E, o),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, E, E, E, o),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, E, E, E, o),
        ]

    def c(self):
        E = self.emoji
        o = self.space
        return [
            '{}{}{}{}{}'.format(o, E, E, E, o),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, o),
            '{}{}{}{}{}'.format(E, o, o, o, o),
            '{}{}{}{}{}'.format(E, o, o, o, o),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(o, E, E, E, o),
        ]

    def d(self):
        E = self.emoji
        o = self.space
        return [
            '{}{}{}{}{}'.format(E, E, E, E, o),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, E, E, E, o),
        ]

    def e(self):
        E = self.emoji
        o = self.space
        return [
            '{}{}{}{}{}'.format(E, E, E, E, E),
            '{}{}{}{}{}'.format(E, o, o, o, o),
            '{}{}{}{}{}'.format(E, o, o, o, o),
            '{}{}{}{}{}'.format(E, E, E, E, o),
            '{}{}{}{}{}'.format(E, o, o, o, o),
            '{}{}{}{}{}'.format(E, o, o, o, o),
            '{}{}{}{}{}'.format(E, E, E, E, E),
        ]

    def f(self):
        E = self.emoji
        o = self.space
        return [
            '{}{}{}{}{}'.format(E, E, E, E, E),
            '{}{}{}{}{}'.format(E, o, o, o, o),
            '{}{}{}{}{}'.format(E, o, o, o, o),
            '{}{}{}{}{}'.format(E, E, E, E, o),
            '{}{}{}{}{}'.format(E, o, o, o, o),
            '{}{}{}{}{}'.format(E, o, o, o, o),
            '{}{}{}{}{}'.format(E, o, o, o, o),
        ]

    def g(self):
        E = self.emoji
        o = self.space
        return [
            '{}{}{}{}{}'.format(o, E, E, E, o),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, o),
            '{}{}{}{}{}'.format(E, o, o, o, o),
            '{}{}{}{}{}'.format(E, o, E, E, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(o, E, E, E, o),
        ]

    def h(self):
        E = self.emoji
        o = self.space
        return [
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, E, E, E, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
        ]

    def i(self):
        E = self.emoji
        o = self.space
        return [
            '{}{}{}{}{}'.format(E, E, E, E, E),
            '{}{}{}{}{}'.format(o, o, E, o, o),
            '{}{}{}{}{}'.format(o, o, E, o, o),
            '{}{}{}{}{}'.format(o, o, E, o, o),
            '{}{}{}{}{}'.format(o, o, E, o, o),
            '{}{}{}{}{}'.format(o, o, E, o, o),
            '{}{}{}{}{}'.format(E, E, E, E, E),
        ]

    def j(self):
        E = self.emoji
        o = self.space
        return [
            '{}{}{}{}{}'.format(E, E, E, E, E),
            '{}{}{}{}{}'.format(o, o, o, o, E),
            '{}{}{}{}{}'.format(o, o, o, o, E),
            '{}{}{}{}{}'.format(o, o, o, o, E),
            '{}{}{}{}{}'.format(o, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(o, E, E, E, o),
        ]

    def k(self):
        E = self.emoji
        o = self.space
        return [
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, E, o),
            '{}{}{}{}{}'.format(E, o, E, o, o),
            '{}{}{}{}{}'.format(E, E, o, o, o),
            '{}{}{}{}{}'.format(E, o, E, o, o),
            '{}{}{}{}{}'.format(E, o, o, E, o),
            '{}{}{}{}{}'.format(E, o, o, o, E),
        ]

    def l(self):
        E = self.emoji
        o = self.space
        return [
            '{}{}{}{}{}'.format(E, o, o, o, o),
            '{}{}{}{}{}'.format(E, o, o, o, o),
            '{}{}{}{}{}'.format(E, o, o, o, o),
            '{}{}{}{}{}'.format(E, o, o, o, o),
            '{}{}{}{}{}'.format(E, o, o, o, o),
            '{}{}{}{}{}'.format(E, o, o, o, o),
            '{}{}{}{}{}'.format(E, E, E, E, E),
        ]

    def m(self):
        E = self.emoji
        o = self.space
        return [
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, E, o, E, E),
            '{}{}{}{}{}'.format(E, o, E, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
        ]

    def n(self):
        E = self.emoji
        o = self.space
        return [
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, E, o, o, E),
            '{}{}{}{}{}'.format(E, o, E, o, E),
            '{}{}{}{}{}'.format(E, o, o, E, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
        ]

    def o(self):
        E = self.emoji
        o = self.space
        return [
            '{}{}{}{}{}'.format(o, E, E, E, o),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(o, E, E, E, o),
        ]

    def p(self):
        E = self.emoji
        o = self.space
        return [
            '{}{}{}{}{}'.format(E, E, E, E, o),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, E, E, E, o),
            '{}{}{}{}{}'.format(E, o, o, o, o),
            '{}{}{}{}{}'.format(E, o, o, o, o),
            '{}{}{}{}{}'.format(E, o, o, o, o),
        ]

    def q(self):
        E = self.emoji
        o = self.space
        return [
            '{}{}{}{}{}'.format(o, E, E, E, o),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, E, o, E),
            '{}{}{}{}{}'.format(E, o, o, E, o),
            '{}{}{}{}{}'.format(o, E, E, o, E),
        ]

    def r(self):
        E = self.emoji
        o = self.space
        return [
            '{}{}{}{}{}'.format(E, E, E, E, o),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, E, E, E, o),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
        ]


    def s(self):
        E = self.emoji
        o = self.space
        return [
            '{}{}{}{}{}'.format(o, E, E, E, o),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, o),
            '{}{}{}{}{}'.format(o, E, E, E, o),
            '{}{}{}{}{}'.format(o, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(o, E, E, E, o),
        ]

    def t(self):
        E = self.emoji
        o = self.space
        return [
            '{}{}{}{}{}'.format(E, E, E, E, E),
            '{}{}{}{}{}'.format(o, o, E, o, o),
            '{}{}{}{}{}'.format(o, o, E, o, o),
            '{}{}{}{}{}'.format(o, o, E, o, o),
            '{}{}{}{}{}'.format(o, o, E, o, o),
            '{}{}{}{}{}'.format(o, o, E, o, o),
            '{}{}{}{}{}'.format(o, o, E, o, o),
        ]

    def u(self):
        E = self.emoji
        o = self.space
        return [
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(o, E, E, E, o),
        ]

    def v(self):
        E = self.emoji
        o = self.space
        return [
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(o, E, o, E, o),
            '{}{}{}{}{}'.format(o, o, E, o, o),
        ]

    def w(self):
        E = self.emoji
        o = self.space
        return [
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, E, o, E),
            '{}{}{}{}{}'.format(E, o, E, o, E),
            '{}{}{}{}{}'.format(o, E, o, E, o),
        ]

    def x(self):
        E = self.emoji
        o = self.space
        return [
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(o, E, o, E, o),
            '{}{}{}{}{}'.format(o, o, E, o, o),
            '{}{}{}{}{}'.format(o, E, o, E, o),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
        ]

    def y(self):
        E = self.emoji
        o = self.space
        return [
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(o, E, o, E, o),
            '{}{}{}{}{}'.format(o, o, E, o, o),
            '{}{}{}{}{}'.format(o, o, E, o, o),
            '{}{}{}{}{}'.format(o, o, E, o, o),
            '{}{}{}{}{}'.format(o, o, E, o, o),
        ]

    def z(self):
        E = self.emoji
        o = self.space
        return [
            '{}{}{}{}{}'.format(E, E, E, E, E),
            '{}{}{}{}{}'.format(o, o, o, o, E),
            '{}{}{}{}{}'.format(o, o, o, E, o),
            '{}{}{}{}{}'.format(o, o, E, o, o),
            '{}{}{}{}{}'.format(o, E, o, o, o),
            '{}{}{}{}{}'.format(E, o, o, o, o),
            '{}{}{}{}{}'.format(E, E, E, E, E),
        ]
