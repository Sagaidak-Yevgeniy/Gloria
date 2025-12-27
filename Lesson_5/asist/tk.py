<<<<<<< HEAD
import tkinter as tk
from PIL import Image, ImageTk
import os
import threading
import time

# Пути к изображениям
emotion_paths = {
    "happy":     "C:/Users/tanku/OneDrive/Desktop/asist/emotions/emotions/happy.png",
    "sad":       "C:/Users/tanku/OneDrive/Desktop/asist/emotions/emotions/sad.png",
    "angry":     "C:/Users/tanku/OneDrive/Desktop/asist/emotions/emotions/angry.png",
    "neutral":   "C:/Users/tanku/OneDrive/Desktop/asist/emotions/emotions/neutral.png",
    "surprised": "C:/Users/tanku/OneDrive/Desktop/asist/emotions/emotions/surprised.png",
    "fearful":   "C:/Users/tanku/OneDrive/Desktop/asist/emotions/emotions/fearful.png",
    "disgusted": "C:/Users/tanku/OneDrive/Desktop/asist/emotions/emotions/disgusted.png",
}

# Глобальная переменная для доступа к GUI
global_emotion_app = None

class EmotionApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg="black")
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        self.label = tk.Label(self.root, bg="black")
        self.label.pack(fill="both", expand=True)

        self.root.bind("<Escape>", lambda e: self.root.destroy())
        self.current_emotion = None

        # Начальное фото
        self.update_emotion("neutral")

    def update_emotion(self, emotion_key):
        path = emotion_paths.get(emotion_key)
        if not path or not os.path.exists(path):
            print(f"❌ Эмоция '{emotion_key}' не найдена.")
            return

        try:
            img = Image.open(path)
            img = img.resize((self.screen_width, self.screen_height), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            self.label.config(image=photo)
            self.label.image = photo
            self.current_emotion = emotion_key
        except Exception as e:
            print(f"Ошибка загрузки: {e}")

    def run(self):
        self.root.mainloop()

# 🔄 Функция, которую можно вызывать из любой точки кода
def set_emotion(emotion_key):
    global global_emotion_app
    if global_emotion_app:
        global_emotion_app.update_emotion(emotion_key)
    else:
        print("⚠️ GUI ещё не инициализирован.")


# ⏱ Пример использования — можно вызывать где угодно
def test():
    time.sleep(2)
    set_emotion("happy")
    time.sleep(2)
    set_emotion("sad")
    time.sleep(2)
    set_emotion("surprised")

# 🔁 Пример вызова в отдельном потоке
threading.Thread(target=test).start()
=======
import tkinter as tk
from PIL import Image, ImageTk
import os
import threading
import time

# Пути к изображениям
emotion_paths = {
    "happy":     "C:/Users/tanku/OneDrive/Desktop/asist/emotions/emotions/happy.png",
    "sad":       "C:/Users/tanku/OneDrive/Desktop/asist/emotions/emotions/sad.png",
    "angry":     "C:/Users/tanku/OneDrive/Desktop/asist/emotions/emotions/angry.png",
    "neutral":   "C:/Users/tanku/OneDrive/Desktop/asist/emotions/emotions/neutral.png",
    "surprised": "C:/Users/tanku/OneDrive/Desktop/asist/emotions/emotions/surprised.png",
    "fearful":   "C:/Users/tanku/OneDrive/Desktop/asist/emotions/emotions/fearful.png",
    "disgusted": "C:/Users/tanku/OneDrive/Desktop/asist/emotions/emotions/disgusted.png",
}

# Глобальная переменная для доступа к GUI
global_emotion_app = None

class EmotionApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg="black")
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        self.label = tk.Label(self.root, bg="black")
        self.label.pack(fill="both", expand=True)

        self.root.bind("<Escape>", lambda e: self.root.destroy())
        self.current_emotion = None

        # Начальное фото
        self.update_emotion("neutral")

    def update_emotion(self, emotion_key):
        path = emotion_paths.get(emotion_key)
        if not path or not os.path.exists(path):
            print(f"❌ Эмоция '{emotion_key}' не найдена.")
            return

        try:
            img = Image.open(path)
            img = img.resize((self.screen_width, self.screen_height), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            self.label.config(image=photo)
            self.label.image = photo
            self.current_emotion = emotion_key
        except Exception as e:
            print(f"Ошибка загрузки: {e}")

    def run(self):
        self.root.mainloop()

# 🔄 Функция, которую можно вызывать из любой точки кода
def set_emotion(emotion_key):
    global global_emotion_app
    if global_emotion_app:
        global_emotion_app.update_emotion(emotion_key)
    else:
        print("⚠️ GUI ещё не инициализирован.")


# ⏱ Пример использования — можно вызывать где угодно
def test():
    time.sleep(2)
    set_emotion("happy")
    time.sleep(2)
    set_emotion("sad")
    time.sleep(2)
    set_emotion("surprised")

# 🔁 Пример вызова в отдельном потоке
threading.Thread(target=test).start()
>>>>>>> 2966b74bb9f1d541460a6175f52c9ffb3311c9b7
