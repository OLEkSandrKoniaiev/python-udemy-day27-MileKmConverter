from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# # Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
# my_label.pack(side="left")
my_label.pack()

# # how to update label
my_label["text"] = "New Text"
my_label.config(text="New Text")


# # Button
def button_clicked():
    # print("I got clicked")
    # my_label.config(text="Button got clicked")
    my_label.config(text=my_entry.get())


my_button = Button(text="Click me", command=button_clicked)
my_button.pack()

# # Entry
my_entry = Entry(width=10)
my_entry.pack()



# # Прописуємо в кінці. Код що стосується вікна прописуємо зверху
window.mainloop()
