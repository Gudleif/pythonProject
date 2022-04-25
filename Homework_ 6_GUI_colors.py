import random
import time
import tkinter as tk
import datetime


window = tk.Tk()
window.geometry('600x600')

li_red = []  # список в который добавляется "красный", в случае выдачи красного цвета

li_time_button = [0]  # список в который добавляется временная метка в момента выдачи красного цвета

li_blame = [0]  # метка для определения, что кнопка была нажата (по умолчанию 0)

li_wrong_count = [0]  # список в который добавляется количество нажатий в ложные цвета (по умолчанию 0)

li_name = []  # список вводимых логинов

li_avg_time = []  # список с добавлением времени всех "красных" нажатий

li_true_count = [0]  # список количества верных нажатий (на красный)

li_range = []  # список добавления значений из функции перебора чисел

# область ввода логина
entry = tk.Entry()
entry.place(x=20, y=100)
entry.pack()


# пространство цветов
# label = tk.Label(height=10, width=600,  text='Color')
# label.pack()

# пространство вывода количества ложных нажатий
label_1 = tk.Label(height=3, width=40, bg='grey')
label_1.pack()

# пространство вывода времени нажатия при красном цвете
label_2 = tk.Label(height=3, width=40, bg='grey')
label_2.pack()

# пространство вывода процентного соотношения результатов
label_3 = tk.Label(height=3, width=40, bg='grey')
label_3.pack()


# функция обработки временных меток и вывода скорости нажатия при появлении красного цвета
def time_button():
    li_blame.insert(0, 1)
    wrong_color()
    percent()
    t = time.time()
    t_1 = float(li_time_button[0])
    t_2 = round((t - t_1), 2)
    t_3 = f'"time of click: " {t_2}'
    li_avg_time.append(t_2)
    print(li_avg_time)
    label_2.config(text=t_3)


# кнопка запуска функции обработки временных меток
button = tk.Button(width=10, height=5, command=time_button, text='Red')
button.pack()


# функция определения процентного соотношения верных и неверных нажатий, сохранения в файл
def percent():
    one = li_wrong_count[0]
    two = li_true_count[0]
    both = one + two
    one_1 = round((one / both * 100), 2)
    two_1 = round((two / both * 100), 2)
    print(one_1, two_1)
    perc = f'wrong percent: {one_1}    true percent: {two_1}'
    label_3.config(text=perc)
    return two_1 - one_1


# функция сохранения данных
def save():
    if percent() > 0:
        file = open('data users.txt', 'a')
        file.write(f'\n name of user: {li_name[0]}, average time : {avg()}, best time: {best_time()}, date of test: {time_now()}')
        file.close()


# кнопка сохранения результатов
button_save = tk.Button(width=10, height=5, command=save, text='save')
button_save.pack()


# функция вычисления среднего времени нажатия на красную кнопку
def avg():
    summ = li_avg_time[0:]
    summ_1 = sum(summ)
    lenn = len(summ)
    avgg = round((summ_1/lenn), 2)
    return avgg


# функция получения лучшего времени
def best_time():
    best = li_avg_time[0]
    for i in range(1, len(li_avg_time)):
        if li_avg_time[i] < best:
            best = li_avg_time[i]
            print(best)
            return best


# функция возвращения времени окончания теста
def time_now():
    date_now = datetime.datetime.now()
    print(date_now)
    return date_now


# перебор чисел для анализа наличия цифр в логине
def rangee():
    x = 0
    for i in range(0,10):
        x += 1
        x_1 = str(x)
        li_range.append(x_1)
    print(li_range)


# функция получения логина из области ввода и добавления в список
def entryy():
    gett = entry.get()
    li_name.insert(0, gett)
    del li_name[1:]
    print(li_name)
    lenn = len(li_name[0])
    listt = list(li_name[0])
    rangee()
    for i in listt[0:]:
        print(i)
        if i not in li_range and lenn > 2:
            rand_colors()


# кнопка запуска функции для получения логина
button_1 = tk.Button(width=5, height=1, command=entryy, text='start')
button_1.pack()


# функция определения соответствия красного цвета для добавления временной метки в список
def timee_1():
    if li_red[0] == 'red':
        li_true_count[0] += 1
        # del li_wrong_count[::]
        # li_wrong_count.insert(0, 0)
        t1 = time.time()
        li_time_button.append(t1)


# функция обработки ложных нажатий
def wrong_color():
    if li_blame[0] == 1 and li_red[0] != 'red':
        li_wrong_count[0] += 1
        ret = f'"count wrong colors: " {li_wrong_count[0]}'
        label_1.config(text=ret)
        del li_blame[::]
        li_blame.insert(0, 0)


# функция выдачи случайных цветов
def rand_colors():
    del li_time_button[::]
    colors = ('red', 'blue', 'yellow', 'green')
    rand = random.choice(colors)
    li_red.insert(0, rand)
    # label.config(bg=li_red[0])
    button.config(bg=li_red[0])
    timee_1()
    del li_red[1::]
    window.after(5000, rand_colors)


# window.after(0, rand_colors)

window.mainloop()
