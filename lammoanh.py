import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk

# Hàm xóa ảnh
def clear_image():
    global image, original_image, image_path
    image = None
    original_image = None
    image_path = None
    canvas.delete("all")
    blur_slider.set(0)  # Đặt giá trị thanh làm mờ về 0

# Hàm lưu ảnh
def save_image():
    if image is not None:
        filename = filedialog.asksaveasfilename(defaultextension=".png")
        if filename:
            cv2.imwrite(filename, image)

# Hàm hiển thị ảnh trên canvas
def display_image():
    if image is not None:
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, anchor=tk.NW, image=img)
        canvas.image = img

# Hàm chọn ảnh từ tệp tin và thay đổi kích thước ảnh
def select_image():
    global image, original_image, image_path
    file_path = filedialog.askopenfilename()
    if file_path:
        image = cv2.imread(file_path)
        image = cv2.resize(image, (400, 400))  # Thay đổi kích thước ảnh
        original_image = image.copy()
        image_path = file_path
        display_image()
        # Đảm bảo thanh gạc bắt đầu từ giá trị 0 khi chọn ảnh mới
        blur_slider.set(0)

# Hàm cập nhật ảnh khi thanh trượt thay đổi giá trị
def update_blur(value):
    global image
    if original_image is not None:
        blur_amount = blur_slider.get()
        image = cv2.GaussianBlur(original_image, (0, 0), sigmaX=blur_amount)
        display_image()

# Tạo cửa sổ Tkinter
root = tk.Tk()
root.title("Xử lý ảnh")

# Tạo canvas để hiển thị ảnh
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Tạo nút "Chọn ảnh" và đặt giữa cửa sổ
select_button = tk.Button(root, text="Chọn ảnh", command=select_image)
select_button.pack(side=tk.LEFT, pady=10, padx=10)

# Tạo nút "Xóa ảnh" và đặt giữa cửa sổ
clear_button = tk.Button(root, text="Xóa ảnh", command=clear_image)
clear_button.pack(side=tk.LEFT, pady=10, padx=10)

# Tạo nút "Lưu" và đặt giữa cửa sổ
save_button = tk.Button(root, text="Lưu", command=save_image)
save_button.pack(side=tk.LEFT, pady=10, padx=10)

# Tạo thanh trượt để điều chỉnh độ mờ
blur_slider = tk.Scale(root, from_=0, to=10, orient="horizontal", label="Độ mờ",command=update_blur)
blur_slider.set(0)  # Giá trị mặc định
blur_slider.pack(pady=10)

image = None
original_image = None
image_path = None

# Bắt đầu ứng dụng
root.mainloop()
