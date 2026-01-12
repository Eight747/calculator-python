import tkinter as tk


root = tk.Tk()
root.title("Calculator")

e = tk.Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    current = e.get()
    e.delete(0, tk.END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, tk.END)

def button_add():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, tk.END)

def button_add():
    global f_num, math
    f_num = int(e.get())
    math = "+"
    e.delete(0, tk.END)

def button_sub():
    global f_num, math
    f_num = int(e.get())
    math = "-"
    e.delete(0, tk.END)

def button_mul():
    global f_num, math
    f_num = int(e.get())
    math = "*"
    e.delete(0, tk.END)

def button_div():
    global f_num, math
    f_num = int(e.get())
    math = "/"
    e.delete(0, tk.END)

def button_equal():
    second_number = int(e.get())
    e.delete(0, tk.END)

    if math == "+":
        e.insert(0, f_num + second_number)
    elif math == "-":
        e.insert(0, f_num - second_number)
    elif math == "*":
        e.insert(0, f_num * second_number)
    elif math == "/":
        if second_number == 0:
            e.insert(0, "Fehler")
        else:
            e.insert(0, f_num / second_number)

#Number buttons
button_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_plus = tk.Button(root, text="+", padx=40, pady=20, bg="darkorange", command= button_add)
button_min = tk.Button(root, text="-", padx=40, pady=20, command= button_sub, bg="darkorange")
button_x = tk.Button(root, text="x", padx=40, pady=20, command=button_mul, bg="darkorange")
button_devide = tk.Button(root, text="÷", padx=40, pady=20, command=button_div, bg="darkorange")
button_enter = tk.Button(root, text="=", padx=40, pady=20, command=button_equal, bg="darkorange")


button_c = tk.Button(root, text="C", padx=40, pady=20, command=button_click, bg="grey")
button_ac = tk.Button(root, text="AC", padx=40, pady=20, command=button_clear, bg="grey")
button_proz = tk.Button(root, text="%", padx=40, pady=20, command=button_click, bg="grey")

button_c.grid(row=1, column=0)
button_ac.grid(row=1, column=1)
button_proz.grid(row=1, column=2)



button_plus.grid(row=4, column=4)
button_min.grid(row=3, column=4)
button_x.grid(row=2, column=4)
button_devide.grid(row=1, column=4)
button_enter.grid(row=5, column=4)

#Lineup für die Nummer Buttons
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_0.grid(row=5, column=0)




root.mainloop()

