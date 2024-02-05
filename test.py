import tkinter as tk

class Applet(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("TopNews")
        self.geometry("300x200")

        self.label = tk.Label(self, text="Hello, Applet!", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.button = tk.Button(self, text="Click Me", command=self.on_button_click)
        self.button.pack()

    def on_button_click(self):
        self.label.config(text="Button Clicked!")

if __name__ == "__main__":
    app = Applet()
    app.mainloop()
