import tkinter as tk

def show_message():
    # Батырма басылғанда жазбаның мәтінін өзгертеміз
    label.config(text="Сәлем, Python!")

root = tk.Tk()
root.title("Тапсырма 2")
root.geometry("400x300")

# Бос мәтінді жазба құру
label = tk.Label(root, text="", font=("Arial", 16))
label.pack(pady=20) # pack() элементті ортаға автоматты қояды

# Батырма құру. command параметрі басылғанда орындалатын функцияны көрсетеді
button = tk.Button(root, text="Басыңыз", command=show_message)
button.pack(pady=10)

root.mainloop()
