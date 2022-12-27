from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

from EmojiAlphabet import EmojiAlphabet
import pygame
import os


class WhatsappBot:
    status = None
    search_bar_selector = '/html/body/div[1]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div[2]'
    message_input_selector = '#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div.fd365im1.to2l77zo.bbv8nyr4.mwp4sxku.gfz4du6o.ag5g9lrv'

    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load('media/person_online_notification.wav')

        firefox_profile = FirefoxProfile('/home/shri/snap/firefox/common/.mozilla/firefox/5l11qwbb.default-release')

        self.browser = webdriver.Firefox(firefox_profile)

        self.browser.get('https://web.whatsapp.com/')

        print("\nWelcome to the whatsapp bot\n")

    def watch(self, name):
        search_bar = self.browser.find_element(
            By.XPATH,
            self.search_bar_selector
        )

        search_bar.clear()
        search_bar.click()
        search_bar.send_keys(name)
        search_bar.send_keys(Keys.ENTER)

        _status = self.browser.find_element(By.CSS_SELECTOR, '#main > header')
        status = _status.text

        if status.find('online') != -1:
            self.status = 'online'
        else:
            self.status = None

        if status:
            print("{} is {}".format(
                name,
                'Online' if self.status else 'Offline'
                )
            )

    def send_message(self, message, times=1):
        message_field = self.browser.find_element(
            By.CSS_SELECTOR,
            self.message_input_selector
        )
        message_field.clear()
        message_field.click()

        for t in range(times):
            message_field.send_keys(message)
            message_field.send_keys(Keys.ENTER)

    def send_emoji_message(self, emoji, message):
        message_field = self.browser.find_element_by_css_selector(
            self.message_input_selector)
        message_field.clear()
        message_field.click()
        emoji = EmojiAlphabet(emoji)

        # Since we have only uppercase emoji alphabets
        # converting the message to uppercase.
        message = message.upper()

        for m in message:
            emoji_generator = {
                'A': emoji.A,
                'B': emoji.B,
                'C': emoji.C,
                'D': emoji.D,
                'E': emoji.E,
                'F': emoji.F,
                'G': emoji.G,
                'H': emoji.H,
                'I': emoji.I,
                'J': emoji.J,
                'K': emoji.K,
                'L': emoji.L,
                'M': emoji.M,
                'N': emoji.N,
                'O': emoji.O,
                'P': emoji.P,
                'Q': emoji.Q,
                'R': emoji.R,
                'S': emoji.S,
                'T': emoji.T,
                'U': emoji.U,
                'V': emoji.V,
                'W': emoji.W,
                'X': emoji.X,
                'Y': emoji.Y,
                'Z': emoji.Z,
                ' ': emoji.heart,
            }

            emoji_pieces = emoji_generator[m]()
            for e in emoji_pieces:
                # Todo
                # Show percentage of work done/ emojis sent.
                message_field.send_keys(e)
                actions = ActionChains(self.browser)
                actions.key_down(
                    Keys.SHIFT
                ).send_keys(Keys.ENTER).key_up(Keys.SHIFT).perform()
                actions.reset_actions()
            message_field.send_keys(Keys.ENTER)


def main():
    bot = WhatsappBot()

    menu = """
    =================== M E N U ======================
        spy: To spy if someone is online.\n
        send message:Send someone message\n
        change name: change to different person\n
        emoji: send emojis as alphabets.
    ==================================================
    """

    name = input("Select a name»\t")

    # TODO handle this with ctrl c signal and exit.
    while True:
        print(menu)
        sub_menu = input("What to do with {}. »\t".format(name))
        os.system('clear')

        if sub_menu == 'spy':
            bot.watch(name)
        elif sub_menu == 'change name':
            name = input("Enter new name »\t")
            bot.watch(name)
        elif sub_menu == 'send message':
            bot.watch(name)
            message = input("Enter the message you want to send »\t")
            times = int(input("Enter number of times you want to send it »\t"))
            bot.send_message(message, times)
        elif sub_menu == 'emoji':
            bot.watch(name)
            message = input("Enter the message you want to send »\t")
            emojis = {
                'cake': '🎂',
                'partyface': '🥳',
                'partypooper': '🎉',
                'kiss': '😚',
                'laugh': '😂',
                'heart': '❤️',
            }
            print(
                """
                type "cake" for {}\n
                type partyface for {}\n
                type partypooper for {}\n
                type kiss for {}\n
                type laugh for {}\n
                type heart for {}\n
                """.format(
                    emojis['cake'],
                    emojis['partyface'],
                    emojis['partypooper'],
                    emojis['kiss'],
                    emojis['laugh'],
                    emojis['heart']
                )
            )
            emoji_key = input("Emoji to use? »\t")
            emoji = emojis.get(emoji_key, '😀')
            bot.send_emoji_message(emoji, message)
        else:
            print("Enter valid option,\n")


if __name__ == "__main__":
    main()
