import tkinter as tk
import numpy as np
import pandas as pd
from tkinter import messagebox

# Hàm tạo hệ các phương trình
def create(entry):
    result.delete(1.0, tk.END)
    delete_fields()
    # Xóa các trường cũ trước khi tạo mới
    num_equations = int(entry.get())

    for i in range(num_equations):
        label = tk.Label(window, text=f"Phương trình {i + 1}:")
        label.grid(row=i + 5, column=0)
        attached_labels.append(label)

        # Lưu trữ các hệ số của phương trình
        equation_entries = []

        for j in range(num_equations + 1):
            entry = tk.Entry(window)
            entry.grid(row=i + 5, column=j + 1)
            equation_entries.append(entry)

        # Lưu trữ các phương trình
        equation_entries_list.append(equation_entries)

# Hàm xóa các hệ phương trình
def delete_fields():
    for entry_list in equation_entries_list:
        for entry in entry_list:
            # Xóa từng entry một
            entry.grid_forget()

    equation_entries_list.clear()
    hide_attached_labels()  # Ẩn các label đính kèm

# Hàm xóa nhãn của từng phương trình tạo ra
def hide_attached_labels():
    for label in attached_labels:
        label.grid_forget()

    attached_labels.clear()

# Kiểm tra dữ liệu hợp lệ
def validate_input(entry):
    try:
        num_equations = int(entry.get())
        if num_equations <= 0 or num_equations > 10:
            raise ValueError("Nhập lại số phương trình hợp lệ.")
        return True

    except ValueError:
        messagebox.showerror("Error", "Nhập lại số phương trình hợp lệ.")
        return False

# Reset dữ liệu hiện tại
def reset(entry):
    entry.delete(0, tk.END)
    entry.insert(0, "")
    delete_fields()
    result.delete(1.0, tk.END)
    hide_attached_labels()

# Giải hệ phương trình vừa tạo
def solve(entry):
    try:
        coefficients = []
        results = []

        for entry_list in equation_entries_list:
            equation_coefficients = []
            for entry in entry_list[:-1]:
                val = float(entry.get())
            # Lưu các các hệ số của phương trình
                equation_coefficients.append(val)
            coefficients.append(equation_coefficients)

            result_val = float(entry_list[-1].get())
            results.append(result_val)

        A = np.array(coefficients)
        B = np.array(results)
        x = np.linalg.solve(A, B)

        result.delete(1.0, tk.END)
        result.insert(tk.END, "Kết quả:\n")
        for i, val in enumerate(x):
            result.insert(tk.END, f"x{i + 1} = {val}\n")

    except Exception as e:
        messagebox.showerror("Error", str(e))


