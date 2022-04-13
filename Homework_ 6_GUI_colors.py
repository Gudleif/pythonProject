import random
import time
import tkinter as tk
window = tk.Tk()
window.geometry('600x600')

li_red = [] #список в который добавляется "красный", в случае выдачи красного цвета

li_time_button = [] #список в который добавляется временная метка в момента выдачи красного цвета

li_blame = [0] #метка для определения, что кнопка была нажата (по умолчанию 0)

li_wrong_count = [0]  #список в который добавляется количество нажатий в ложные цвета (по умолчанию 0)

    #пространство цветов
label = tk.Label(height=10, width=600,  text='Color')
label.pack()

    #пространство вывода количества ложных нажатий
label_1 = tk.Label(height=3, width=40, bg='green')
label_1.pack()

    #пространство вывода времени нажатия при красном цвете
label_2 = tk.Label(height=3, width=40, bg='green')
label_2.pack()

    #функция обработки временных меток и вывода скорости нажатия при появлении красного цвета
def time_button():
    li_blame.insert(0, 1)
    wrong_color()
    t = time.time()
    t_1 = float(li_time_button[0])
    t_2 = (t - t_1)
    t_3 = (f'"time of click: " {t_2}')
    label_2.config(text= t_3)

    #кнопка запуска функции обработки временных меток
button = tk.Button( width= 20, height= 10, command= time_button, text= 'Red' , fg= 'red')
button.pack()

    #функция определения соответствия красного цвета для добавления временной метки в список
def timee_1():
    if li_red[0] == 'red':
        del li_wrong_count[::]
        li_wrong_count.insert(0, 0)
        t1 = time.time()
        li_time_button.append(t1)

    #функция обработки ложных нажатий
def wrong_color():
    if li_blame[0] == 1 and li_red[0] != 'red':
        li_wrong_count[0] += 1
        ret = (f'"count wrong colors: " {li_wrong_count[0]}')
        label_1.config(text=ret)
        del li_blame[::]
        li_blame.insert(0, 0)

    #функция выдачи случайных цветов
def rand_colors():
    del li_time_button[::]
    colors = ('red', 'blue', 'yellow', 'green')
    rand = random.choice(colors)
    li_red.insert(0, (rand))
    label.config(bg=li_red[0])
    timee_1()
    del li_red[1::]
    window.after(5000, rand_colors)


window.after(0, rand_colors)

window.mainloop()
