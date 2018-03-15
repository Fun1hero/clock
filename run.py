import tkinter as tk
import datetime


# fill on = AM
# empty on = PM

x = 150
switch_f = False
minute_f = False
counter = 0


def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)


tk.Canvas.create_circle = _create_circle


def _create_circle_arc(self, x, y, r, **kwargs):
    if "start" in kwargs and "end" in kwargs:
        kwargs["extent"] = kwargs["end"] - kwargs["start"]
        del kwargs["end"]
    return self.create_arc(x-r, y-r, x+r, y+r, **kwargs)


tk.Canvas.create_circle_arc = _create_circle_arc


def time():
    global x
    global switch_f
    global minute_f
    global counter
    csv.delete('all')

    hr_col = '#6699CC'
    mn_col = '#003366'
    sc_col = '#C0C0C0'

    csv.create_circle(csv.winfo_width() / 2, csv.winfo_height() / 2, 33+x, fill="", dash = '3',
                      outline=sc_col, width=2) #a6a6a6
    csv.create_circle(csv.winfo_width() / 2, csv.winfo_height() / 2, 27+x, fill="", dash = '3',
                      outline=sc_col, width=2) #a6a6a6

    csv.create_circle(csv.winfo_width() / 2, csv.winfo_height() / 2, 43+x, fill="", dash = '3',
                      outline=mn_col, width=2) #00264d
    csv.create_circle(csv.winfo_width() / 2, csv.winfo_height() / 2, 37+x, fill="", dash = '3',
                      outline=mn_col, width=2) #00264d

    csv.create_circle(csv.winfo_width() / 2, csv.winfo_height() / 2, 53+x, fill="", dash = '3',
                      outline=hr_col, width=2) #3973ac
    csv.create_circle(csv.winfo_width() / 2, csv.winfo_height() / 2, 47+x, fill="", dash = '3',
                      outline=hr_col, width=2) #3973ac

    hr = int(datetime.datetime.now().hour)
    mn = int(datetime.datetime.now().minute)
    sc = int(datetime.datetime.now().second)
    msc = int(datetime.datetime.now().microsecond)

    if sc == 0 and switch_f:
        minute_f = not minute_f
        switch_f = False
        print(minute_f)
    elif sc == 1:
        switch_f = True

    if hr > 12:
        hr = hr % 12

    # print('Hour: ' + str(hr) + ' Min: ' + str(mn) + ' Sec: ' + str(sc) + ' Msc: ' + str(msc))
    if minute_f:
        csv.create_circle_arc(csv.winfo_width() / 2, csv.winfo_height() / 2, 30 + x, style="arc", outline=sc_col,
                                  width=8, start=90, end=450 - (sc * 6) - (msc * 0.000006))
    else:
        # csv.create_circle_arc(csv.winfo_width() / 2, csv.winfo_height() / 2, 30 + x, style="arc", outline=sc_col,
        #                            width=8, start=90, end=440)
        csv.create_circle_arc(csv.winfo_width() / 2, csv.winfo_height() / 2, 30 + x, style="arc", outline=sc_col,
                                  width=8, start=90, end=90 - (sc * 6) - (msc * 0.000006))

    if mn == 0:
        csv.create_circle(csv.winfo_width() / 2, csv.winfo_height() / 2, 40 + x, fill="",
                          outline=mn_col, width=8)  # 00264d
    else:
        csv.create_circle_arc(csv.winfo_width() / 2, csv.winfo_height() / 2, 40 + x, style="arc",
                              outline=mn_col, width=8, start=450, end=90 - mn * 6)

    if hr == 12:
        csv.create_circle(csv.winfo_width() / 2, csv.winfo_height() / 2, 50 + x, fill="",
                          outline=hr_col, width=8)  # 3973ac
    else:
        csv.create_circle_arc(csv.winfo_width() / 2, csv.winfo_height() / 2, 50 + x, style="arc",
                              outline=hr_col, width=8, start=450, end=90 - hr * 30)

    csv.create_circle(csv.winfo_width() / 4, csv.winfo_height() / 4, ((msc*0.000006)+sc/12),
                      fill="#003366", outline="#C0C0C0", width=1)



    root.after(10, time)


root = tk.Tk()
csv = tk.Canvas(root, width=800, height=800, bg='#000044')
csv.pack()

time()

root.mainloop()
