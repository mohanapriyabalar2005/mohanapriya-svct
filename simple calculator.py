from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry('357x420+0+0')  # Fixed Geometry
        master.config(bg='gray')
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''
        Entry(master, width=17, bg='#fff', font=('Arial', 28), textvariable=self.equation).place(x=0, y=0)

        # Row 1
        Button(master, width=11, height=4, text='(', relief='flat', bg='white', command=lambda: self.show('(')).place(x=0, y=50)
        Button(master, width=11, height=4, text=')', relief='flat', bg='white', command=lambda: self.show(')')).place(x=90, y=50)
        Button(master, width=11, height=4, text='%', relief='flat', bg='white', command=lambda: self.show('%')).place(x=180, y=50)
        Button(master, width=11, height=4, text='/', relief='flat', bg='white', command=lambda: self.show('/')).place(x=270, y=50)

        # Row 2
        Button(master, width=11, height=4, text='7', relief='flat', bg='white', command=lambda: self.show('7')).place(x=0, y=125)
        Button(master, width=11, height=4, text='8', relief='flat', bg='white', command=lambda: self.show('8')).place(x=90, y=125)
        Button(master, width=11, height=4, text='9', relief='flat', bg='white', command=lambda: self.show('9')).place(x=180, y=125)
        Button(master, width=11, height=4, text='*', relief='flat', bg='white', command=lambda: self.show('*')).place(x=270, y=125)

        # Row 3
        Button(master, width=11, height=4, text='4', relief='flat', bg='white', command=lambda: self.show('4')).place(x=0, y=200)
        Button(master, width=11, height=4, text='5', relief='flat', bg='white', command=lambda: self.show('5')).place(x=90, y=200)
        Button(master, width=11, height=4, text='6', relief='flat', bg='white', command=lambda: self.show('6')).place(x=180, y=200)
        Button(master, width=11, height=4, text='-', relief='flat', bg='white', command=lambda: self.show('-')).place(x=270, y=200)

        # Row 4
        Button(master, width=11, height=4, text='1', relief='flat', bg='white', command=lambda: self.show('1')).place(x=0, y=275)
        Button(master, width=11, height=4, text='2', relief='flat', bg='white', command=lambda: self.show('2')).place(x=90, y=275)
        Button(master, width=11, height=4, text='3', relief='flat', bg='white', command=lambda: self.show('3')).place(x=180, y=275)
        Button(master, width=11, height=4, text='+', relief='flat', bg='white', command=lambda: self.show('+')).place(x=270, y=275)

        # Row 5
        Button(master, width=11, height=4, text='0', relief='flat', bg='white', command=lambda: self.show('0')).place(x=0, y=350)
        Button(master, width=11, height=4, text='.', relief='flat', bg='white', command=lambda: self.show('.')).place(x=90, y=350)
        Button(master, width=11, height=4, text='=', relief='flat', bg='lightblue', command=self.solve).place(x=180, y=350)
        Button(master, width=11, height=4, text='C', relief='flat', bg='white', command=self.clear).place(x=270, y=350)

    def show(self, value):
        """Append a character to the input field."""
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        """Clear the input field."""
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        """Evaluate the mathematical expression."""
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
            self.entry_value = str(result)  # Store result for further operations
        except Exception as e:
            self.equation.set("Error")
            self.entry_value = ''

# Run the Calculator
root = Tk()
calculator = Calculator(root)
root.mainloop()
