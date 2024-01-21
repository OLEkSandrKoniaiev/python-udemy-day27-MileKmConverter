from tkinter import *


def button_clicked():
    # print("I got clicked")
    # my_label.config(text="Button got clicked")
    my_label.config(text=my_entry.get())


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

# # Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
# my_label.pack(side="left")
# # how to update label
my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=10, pady=20)

# # Button
my_button = Button(text="Click me", command=button_clicked)
my_button.grid(column=1, row=1)

# # New Button
my_new_button = Button(text="Click me too", command=button_clicked)
my_new_button.grid(column=3, row=0)

# # Entry
my_entry = Entry(width=10)
my_entry.grid(column=4, row=3)

# # Прописуємо в кінці. Код що стосується вікна прописуємо зверху
window.mainloop()

# Трохи теорії: .pack(side="") використовують для розташування об'єктів один за одним. Параметр впливає лише на сторону.
# .place(x=,y=) дає розташування за координатами
# .grid(column=, row=) фактично сітка, як в bootstrap чи figma. Працюватиме коректно коли всі елементи будуть розставлені по місцях
