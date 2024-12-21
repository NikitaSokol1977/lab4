import tkinter as tk
import random
import string

def generate_password():
    """Генерирует пароль на основе выбранных параметров."""
    length = length_scale.get()
    characters = ""
    if use_lowercase.get():
        characters += string.ascii_lowercase
    if use_digits.get():
        characters += string.digits
    if use_special_chars.get():
        characters += "!@#$%^&*()"

    if not characters:
        password_label.config(text="Выберите хотя бы один параметр!")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_label.config(text=password)

def copy_to_clipboard():
    """Копирует сгенерированный пароль в буфер обмена."""
    root.clipboard_clear()
    root.clipboard_append(password_label.cget("text"))
    root.update()

# Создание основного окна
root = tk.Tk()
root.title("Генератор паролей")

# Параметры пароля
use_lowercase = tk.BooleanVar(value=True)
use_digits = tk.BooleanVar(value=True)
use_special_chars = tk.BooleanVar(value=True)

# Виджеты для параметров
lowercase_check = tk.Checkbutton(root, text="Включить буквы нижнего регистра [a-z]", variable=use_lowercase)
lowercase_check.pack(anchor="w")

digits_check = tk.Checkbutton(root, text="Включить цифры [0-9]", variable=use_digits)
digits_check.pack(anchor="w")

special_chars_check = tk.Checkbutton(root, text="Включить спецсимволы [!@#$%]", variable=use_special_chars)
special_chars_check.pack(anchor="w")

# Длина пароля
length_label = tk.Label(root, text="Длина пароля:")
length_label.pack(anchor="w")

length_scale = tk.Scale(root, from_=8, to=32, orient=tk.HORIZONTAL)
length_scale.set(12)
length_scale.pack(anchor="w")

# Кнопка генерации
generate_button = tk.Button(root, text="Сгенерировать пароль", command=generate_password)
generate_button.pack(pady=10)

# Метка для вывода пароля
password_label = tk.Label(root, text="", font=("Arial", 14))
password_label.pack()

# Кнопка копирования
copy_button = tk.Button(root, text="Копировать в буфер", command=copy_to_clipboard)
copy_button.pack(pady=5)

# Запуск главного цикла
root.mainloop()