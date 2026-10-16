import tkinter as tk

def turn_on():
    label.config(text="Мәтін белсенді!")

def turn_off():
    label.config(text="")

root = tk.Tk()
root.title("Тапсырма 3")
root.geometry("400x300")

label = tk.Label(root, text="", font=("Arial", 16))
label.pack(pady=30)

# Қосу және Өшіру батырмалары
btn_on = tk.Button(root, text="Қосу", command=turn_on)
btn_on.pack(side=tk.LEFT, padx=50) # Сол жаққа орналастыру

btn_off = tk.Button(root, text="Өшіру", command=turn_off)
btn_off.pack(side=tk.RIGHT, padx=50) # Оң жаққа орналастыру

root.mainloop()
