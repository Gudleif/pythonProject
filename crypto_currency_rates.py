import requests
import tkinter as tk


class App:
    root = tk.Tk()
    root.geometry('600x600')


class Lab:
    def __init__(self, text):
        self.text = text

    App.label = tk.Label(width=50, height=50, border=2)
    App.label.pack()

    def lab(self):
        App.label.config(text=f'Last price: {self.text} usdt')


class Get(App):
    def __init__(self, text):
        self.text = text

    def conf(self):
        url = 'https://api.binance.com/api/v3/ticker/price?symbol=' + self.text
        get_1 = requests.get(url)
        get_2 = get_1.json()
        get_3 = get_2['price']
        h1 = Lab(get_3)
        h1.lab()


class MainMenu(App):
    menu = tk.Menu(App.root)
    file_menu = tk.Menu(menu, tearoff=0)

    ticker = Get('BTCUSDT')
    ticker_1 = Get('ETHUSDT')
    ticker_2 = Get('LTCUSDT')
    ticker_3 = Get('BNBUSDT')

    file_menu.add_command(label='BTC-USDT', command=ticker.conf)
    file_menu.add_command(label='ETH-USDT', command=ticker_1.conf)
    file_menu.add_command(label='LTC-USDT', command=ticker_2.conf)
    file_menu.add_command(label='BNB-USDT', command=ticker_3.conf)

    menu.add_cascade(label='Currency', menu=file_menu)
    menu.add_command(label='Exit', command=App.root.destroy)

    App.root.config(menu=menu)
    App.root.mainloop()
