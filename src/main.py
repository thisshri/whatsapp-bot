from selenium import webdriver
import pygame
import os
import time


class EmojiAlphabets:
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

    def emoji_string(self, string):
        emoji_generator = {
            'a': self.a,
        }

        emoji_string = []

        for char in string:
            foo = emoji_generator.get(char, "No emoji for this char")
            emoji_string.append(foo())

        # it returns a var which had milti line prints in it.
        return emoji_string


class WhatsappBot:
    status = None
    search_bar_selector = "#side > div._2HS9r > div > label > input"

    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load('./media/person_online_notification.mp3')
        self.browser = webdriver.Chrome()
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
    emojiChar = EmojiAlphabets("😚")
    foo = emojiChar.emoji_string('a')
    print(foo[0])
    import pdb; pdb.set_trace()
    return




    bot = WhatsappBot()

    menu = """
    =================== M E N U ======================
        spy: To spy if someone is online.\n
        spyTill: spy for the mentioned duration.\n
        send message:Send someone message\n
        change name: change to different person\n
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
        else:
            print("Enter valid option,\n")


if __name__ == "__main__":
    main()
