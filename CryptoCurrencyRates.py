import requests
import json
import tkinter as tk
import time


class App:
    root = tk.Tk()
    root.geometry('600x600')

class Lab(App):
    def __init__(self, text):
        self.text = text

    def conf(self):
        url = 'https://api.binance.com/api/v3/ticker/price?symbol=' + self.text
        get_1 = requests.get(url)
        get_2 = get_1.json()
        get_3 = get_2['price']
        print(get_3)


class Rates:
    def __init__(self, text):
        self.text = text

    def prinnt(self):
        print(self.text)
        h1 = Lab(self.text)
        h1.conf()


class MainMenu(App):
    menu = tk.Menu(App.root)
    file_menu = tk.Menu(menu, tearoff=0)

    tiker = Rates('BTCUSDT')
    tiker_1 = Rates('ETHUSDT')
    tiker_2 = Rates('LTCUSDT')
    tiker_3 = Rates('BNBUSDT')

    file_menu.add_command(label='list_rates[0]', command=tiker.prinnt)
    file_menu.add_command(label='list_rates[1]', command=tiker_1.prinnt)
    file_menu.add_command(label='list_rates[2]', command=tiker_2.prinnt)
    file_menu.add_command(label='list_rates[3]', command=tiker_3.prinnt)

    menu.add_cascade(label='Currency', menu=file_menu)
    menu.add_command(label='Exit', command=App.root.destroy)

    App.root.config(menu=menu)
    App.root.mainloop()

if __name__ == '__main__':
    MainMenu