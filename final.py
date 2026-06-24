import tkinter as tk
import math

root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("280x400")
root.resizable(False, False)

expr = ""

display = tk.Entry(root, font=("Arial", 16), justify="right", bd=4)
display.pack(fill="x", padx=8, pady=8, ipady=6)

def press(value):
    global expr
    expr += str(value)
    display.delete(0, tk.END)
    display.insert(tk.END, expr)

def clear():
    global expr
    expr = ""
    display.delete(0, tk.END)

def delete():
    global expr
    expr = expr[:-1]
    display.delete(0, tk.END)
    display.insert(tk.END, expr)

def equal():
    global expr
    try:
        e = expr.replace("π", str(math.pi))
        e = e.replace("e", str(math.e))
        e = e.replace("^", "**")
        result = eval(e)
        display.delete(0, tk.END)
        display.insert(tk.END, result)
        expr = str(result)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
        expr = ""

def scientific(func):
    global expr
    try:
        x = float(expr)

        if func == "sin":
            result = math.sin(math.radians(x))
        elif func == "cos":
            result = math.cos(math.radians(x))
        elif func == "tan":
            result = math.tan(math.radians(x))
        elif func == "log":
            result = math.log10(x)
        elif func == "ln":
            result = math.log(x)
        elif func == "sqrt":
            result = math.sqrt(x)
        elif func == "cbrt":
            result = x ** (1 / 3)
        elif func == "square":
            result = x ** 2
        elif func == "cube":
            result = x ** 3
        elif func == "exp":
            result = math.exp(x)
        elif func == "fact":
            result = math.factorial(int(x))

        display.delete(0, tk.END)
        display.insert(tk.END, result)
        expr = str(result)

    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
        expr = ""

frame = tk.Frame(root)
frame.pack()

buttons = [
    ("C", "red"), ("%", "lightgreen"), ("DEL", "orange"), ("=", "limegreen"),
    ("7", "lightgreen"), ("8", "lightgreen"), ("9", "lightgreen"), ("+", "lightgreen"),
    ("4", "lightgreen"), ("5", "lightgreen"), ("6", "lightgreen"), ("-", "lightgreen"),
    ("1", "lightgreen"), ("2", "lightgreen"), ("3", "lightgreen"), ("*", "lightgreen"),
    ("00", "lightgreen"), ("0", "lightgreen"), (".", "lightgreen"), ("/", "lightgreen"),
    ("x²", "gold"), ("x³", "gold"), ("√x", "gold"), ("∛x", "gold"),
    ("sin", "gold"), ("cos", "gold"), ("tan", "gold"), ("%", "gold"),
    ("log", "gold"), ("ln", "gold"), ("eˣ", "gold"), ("xʸ", "gold"),
    ("π", "gold"), ("e", "gold"), ("!", "gold"), ("(", "gold"),
    (")", "gold")
]

row = 0
col = 0

for text, color in buttons:
    if text == "=":
        cmd = equal
    elif text == "C":
        cmd = clear
    elif text == "DEL":
        cmd = delete
    elif text == "sin":
        cmd = lambda: scientific("sin")
    elif text == "cos":
        cmd = lambda: scientific("cos")
    elif text == "tan":
        cmd = lambda: scientific("tan")
    elif text == "log":
        cmd = lambda: scientific("log")
    elif text == "ln":
        cmd = lambda: scientific("ln")
    elif text == "√x":
        cmd = lambda: scientific("sqrt")
    elif text == "∛x":
        cmd = lambda: scientific("cbrt")
    elif text == "x²":
        cmd = lambda: scientific("square")
    elif text == "x³":
        cmd = lambda: scientific("cube")
    elif text == "eˣ":
        cmd = lambda: scientific("exp")
    elif text == "!":
        cmd = lambda: scientific("fact")
    elif text == "xʸ":
        cmd = lambda: press("^")
    elif text == "%":
        cmd = lambda: press("/100")
    else:
        cmd = lambda t=text: press(t)

    tk.Button(
        frame,
        text=text,
        font=("Arial", 10),
        width=5,
        height=1,
        bg=color,
        command=cmd
    ).grid(row=row, column=col, padx=1, pady=1)

    col += 1
    if col == 4:
        col = 0
        row += 1

root.mainloop()