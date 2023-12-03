# Standard python libraries
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import random


def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text File", "*.txt")])
    file_entry.delete(0, tk.END)
    file_entry.insert(tk.END, file_path)


def select_winners():
    file_path = file_entry.get()
    try:
        num = int(winners_entry.get())
        if num <= 0:
            messagebox.showwarning("خطا", "عدد وارد شده یک عدد صحیح نیست")
            return
    except ValueError:
        messagebox.showwarning("خطا", "لطفا یک عدد وارد کنید")
        return

    try:
        with open(file_path, "r") as file:
            name_list = file.read().splitlines()
            if len(name_list) < num:
                messagebox.showwarning("خطا", "عددی که وارد کرده اید بزرگ تر از تعداد شرکت کننده ها است")
                return
            winners_list = random.sample(name_list, num)
            top_window = tk.Toplevel()
            top_window.title("لیست برندگان")
            top_window.geometry("400x600")
            top_window.resizable(True, True)
            top_window.configure(background="#8BC34A")
            win_label = ttk.Label(top_window, text="برندگان قرعه کشی", font=("Arial", 14),
                                  background="#004D40", foreground="white")
            win_label.pack(pady=15)
            winners_list = [f"{i + 1}- {j}" for i, j in enumerate(winners_list)]
            winners = "\n".join(winners_list)
            show_winners = ttk.Label(top_window, text=winners, font=("Arial", 14),
                                     background="#8BC34A", foreground="#004D40")
            show_winners.pack(pady=15)
            top_window.mainloop()
    except FileNotFoundError:
        messagebox.showwarning("خطا", "!فایل پیدا نشد")
    except Exception as e:
        messagebox.showwarning("خطا", str(e))


# Creating an object from tkinter
window = tk.Tk()

window.title("برنامه قرعه کشی")
window.geometry("500x270")

# For changing the window sizes
window.resizable(True, True)

window.configure(background="#8BC34A")

# Creating a title
file_label = ttk.Label(window, text="فایل اسامی شرکت کنندگان را انتخاب کنید",
                       font=("Arial", 14), background="#8BC34A", foreground="#004D40")
file_label.pack(pady=20)

style = ttk.Style()
style.configure("TFrame", background="#006064")

# Creating a frame
file_frame = ttk.Frame(window, style="TFrame")
file_frame.pack(pady=5)

# Creating an input frame for select the file
file_entry = ttk.Entry(file_frame, font=("Aria", 12))
file_entry.grid(row=0, column=0, padx=5, pady=5)

# Creating a button for select the file input
file_button = ttk.Button(file_frame, text="انتخاب فایل", command=select_file)
file_button.grid(row=0, column=1, padx=2, pady=2)

# Creating a label for winners
winners_label = ttk.Label(window, text="تعداد شرکت کننده ها را وارد کنید",
                          font=("Arial", 14), background="#8BC34A", foreground="#004D40")
winners_label.pack(pady=15)

# Creating an input frame for winners
winners_entry = ttk.Entry(window, font=("Aria", 12), width=5)
winners_entry.pack(pady=5)

# Creating a button for winners input
file_button = ttk.Button(window, text="تایید", command=select_winners)
file_button.pack(pady=5)

# For showing the event loop
window.mainloop()
