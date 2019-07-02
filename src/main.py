from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from EmojiAlphabet import EmojiAlphabet
import pygame
import os


class WhatsappBot:
    status = None
    search_bar_selector = '#side > div._2HS9r > div > label > input'
    message_input_selector = '#main > footer > div._2i7Ej.copyable-area > div._13mgZ > div > div._3u328.copyable-text.selectable-text'

    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load('./media/person_online_notification.mp3')
        self.browser = webdriver.Firefox()
        self.browser.get('https://web.whatsapp.com/')

        print("\nWelcome to the whatsapp bot\n")

    def watch(self, name):
        search_bar = self.browser.find_element_by_css_selector(
            self.search_bar_selector)
        search_bar.clear()
        search_bar.click()
        search_bar.send_keys(name)
        # press enter to search the person.
        search_bar.send_keys(u'\ue007')

        _status = self.browser.find_element_by_css_selector('#main > header')
        status = _status.text

        if status.find('online') != -1:
            self.status = 'online'
        else:
            self.status = None
        
        if status:
            print("{} is {}".format(name, 'Online' if self.status else 'Offline'))

    def send_message(self, message, times=1):
        message_field = self.browser.find_element_by_css_selector(
            self.message_input_selector)
        message_field.clear()
        message_field.click()

        for t in range(times):
            message_field.send_keys(message)
            message_field.send_keys(u'\ue007')

    def send_emoji_message(self, emoji, message):
        message_field = self.browser.find_element_by_css_selector(
            self.message_input_selector)
        message_field.clear()
        message_field.click()
        emoji = EmojiAlphabet("🎂")
        
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
            }

            emoji_pieces = emoji_generator[m]()
            for e in emoji_pieces:
                print("= START =")
                print(e)
                print("= END =")
                message_field.send_keys(e)
                actions = ActionChains(self.browser)
                actions.key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT).perform()
                actions.reset_actions()
            message_field.send_keys(Keys.ENTER)


"""
    def keepWatching(self, name, num):
        print("++++++++++++++++++++++ web.whatsapp scrapping started ++++++++++++++++++++++")

        for x in range(num):
            #wait for 30 secs
            time.sleep(10)
            #call watch(name)
            watch(name);
            print("staus is : ",STATUS)
            if (STATUS == "online"):
                #play the sound
                pygame.mixer.music.play()
            else:
                print(name," is offline")
 """


def main():
    bot = WhatsappBot()

    menu = """
    =================== M E N U ======================
        spy: To spy if someone is online.\n
        spyTill: spy for the mentioned duration.\n
        send message:Send someone message\n
        change name: change to different person\n
        emoji: send emojis as alphabets.
    ==================================================
    """

    name = input("Select a name»\t")

    # TODO handle this with ctrl c signal and exit.
    while True:
        print(menu)
        sub_menu = input("Choose what do you want to do with {}. »\t".format(name))
        os.system('clear')

        if sub_menu == 'spy':
            bot.watch(name)
        elif sub_menu == 'change name':
            name = input("Enter new name »\t")
            bot.watch(name)
        elif sub_menu == 'send message':
            message = input("Enter the message you want to send »\t")
            times = input("Enter number of times you want to send it »\t")
            bot.send_message(message, times)
        elif sub_menu == 'emoji':
            message = input("Enter the message you want to send »\t")
            bot.send_emoji_message("😀", message)
        else:
            print("Enter valid option,\n")


if __name__ == "__main__":
    main()
