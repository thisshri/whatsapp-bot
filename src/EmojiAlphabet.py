class EmojiAlphabet:
    space = "　  "
    fill_white_space = "🙈"

    def __init__(self, emoji):
        self.emoji = emoji

    def A(self):
        E = self.emoji
        o = self.space
        ws = self.fill_white_space
        return [
            '{}{}{}{}{}'.format(ws, E, E, E, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, E, E, E, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
        ]

    def B(self):
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

    def C(self):
        E = self.emoji
        o = self.space
        ws = self.fill_white_space
        return [
            '{}{}{}{}{}'.format(ws, E, E, E, o),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, o),
            '{}{}{}{}{}'.format(E, o, o, o, o),
            '{}{}{}{}{}'.format(E, o, o, o, o),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(o, E, E, E, o),
        ]

    def D(self):
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

    def E(self):
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

    def F(self):
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

    def G(self):
        E = self.emoji
        o = self.space
        ws = self.fill_white_space
        return [
            '{}{}{}{}{}'.format(ws, E, E, E, o),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, o),
            '{}{}{}{}{}'.format(E, o, o, o, o),
            '{}{}{}{}{}'.format(E, o, E, E, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(o, E, E, E, o),
        ]

    def H(self):
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

    def I(self):
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

    def J(self):
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

    def K(self):
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

    def L(self):
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

    def M(self):
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

    def N(self):
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

    def O(self):
        E = self.emoji
        o = self.space
        ws = self.fill_white_space
        return [
            '{}{}{}{}{}'.format(ws, E, E, E, o),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(o, E, E, E, o),
        ]

    def P(self):
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

    def Q(self):
        E = self.emoji
        o = self.space
        ws = self.fill_white_space
        return [
            '{}{}{}{}{}'.format(ws, E, E, E, o),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, E, o, E),
            '{}{}{}{}{}'.format(E, o, o, E, o),
            '{}{}{}{}{}'.format(o, E, E, o, E),
        ]

    def R(self):
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

    def S(self):
        E = self.emoji
        o = self.space
        ws = self.fill_white_space
        return [
            '{}{}{}{}{}'.format(ws, E, E, E, o),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, o),
            '{}{}{}{}{}'.format(o, E, E, E, o),
            '{}{}{}{}{}'.format(o, o, o, o, E),
            '{}{}{}{}{}'.format(E, o, o, o, E),
            '{}{}{}{}{}'.format(o, E, E, E, o),
        ]

    def T(self):
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

    def U(self):
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

    def V(self):
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

    def W(self):
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

    def X(self):
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

    def Y(self):
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

    def Z(self):
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
