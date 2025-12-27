import os
from random import randint
import script.commands as cm
import pygame
from datetime import datetime
import json  # библиотека для распознавания речи
import pyaudio  # библиотека для распознавания речи
from vosk import Model, KaldiRecognizer  # библиотека для распознавания речи
from silero_tts.silero_tts import SileroTTS
import g4f


# import RPi.GPIO as GPIO
# import alsaaudio

model = Model('model_small')
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()


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



def listen():
    """
    Функция listen дает возможность постоянно слушать микрофон

    :return:
    """
    try:
        while True:
            data = stream.read(8000)
            if (rec.AcceptWaveform(data)) and (len(data) > 0):
                answer = json.loads(rec.Result())
                if answer['text']:
                    yield answer['text']
    except ImportError:
        print('Ошибка в функции (listen)')


def play_music(file):
    """
    Функция play_music ает возможность проигрывать аудио файлы.
    :param file:
    :return:
    """
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
    except ImportError:
        print('Ошибка в функции(play_music)')


def word_filter():
    """
    Функция word_filter дает возможность фильтровать слова, а также уменьшать или увеличивать звук.
    :return:
    """
    try:
        for text in listen():
            print(text)
            """
            if 'сто' in text:
                mix.setvolume(100)  # 100
            if 'девяносто' in text:
                mix.setvolume(90)  # 90
            if 'восемьдесят' in text:
                mix.setvolume(80)  # 80
            if 'семьдесят' in text:
                mix.setvolume(70)  # 70
            if 'шестьдесят' in text:
                mix.setvolume(60)  # 60
            if 'пятьдесят' in text:
                mix.setvolume(50)  # 50
            if 'сорок' in text:
                mix.setvolume(40)  # 40
            if 'тридцать' in text:
                mix.setvolume(30)  # 30
            if 'двадцать' in text:
                mix.setvolume(20)  # 20
            if 'десять' in text:
                mix.setvolume(10)  # 10
            if 'ноль' in text:
                mix.setvolume(0)  # 0
            """
            yield text
    except ImportError:
        print('Ошибка в функции(world_filter)')


def haw_are_you():
    """
    Функция haw_are_you дает возможность отвечать на вопросы "как дела"
    а также спрашивать у пользователя как у него дела.

    :return:
    """
    try:
        print('Находится в функции haw_are_you')
        a = randint(0, 4)
        if a == 1:
            # хорошо, а как у вас
            play_music('speech synthesis/haw_are_you/хорошо_а_как_у_вас.wav')
        elif a == 2:
            # неплохо, как у вас
            play_music('speech synthesis/haw_are_you/неплохо_как у_вас.wav')
        elif a == 3:
            pass
            # система не дает сбой как говорится гуд, а как у вас
            play_music('speech synthesis/haw_are_you/система_не_дает_сбой_как_говорится_гуд,_а_как_у_вас.wav')
        elif a == 4:
            pass
            # вполне нормально, как у вас
        for text in word_filter():
            if text in cm.commands['плохое_настроение']:
                # это печально, можете позвонить на номер 150 работает 24 на 7
                play_music('speech synthesis/haw_are_you/это печально, можете позвонить на номер 150 работает 24 на '
                           '7.wav')
                break
            if text in cm.commands['хорошее_настроение']:
                # звук радости
                play_music('speech synthesis/sounds/звук_радости.mp3')
                break
        main()
    except ImportError:
        print('Ошибка в функции(haw_are_you)')


def about_the_robot():
    """

    :return:
    """
    try:
        print('Находится в функции about_the_robot')
        # Я Глория голосовой ассистент помощник, которой поможет вам выполнить ваши ежедневные задачи вы можете
        # поговорить со мной когда вам скучно, могу рассказать сказку ребенку, а так же поиграть с вашим домашними
        # животными
        play_music('speech synthesis/about_the_robot/Я_Глория_голосовой_ассистент_помощник.wav')
        main()
    except ImportError:
        print('Ошибка в функции(about_the_robot)')


def name():
    """

    :return:
    """
    try:
        print('Находится в функции name')
        # Глория
        play_music('speech synthesis/name/Я_Глория.wav')
        # Могу ли я чем то вам помочь
        play_music('speech synthesis/name/Могу_ли_я_чем_то_вам_помочь.wav')
        main()
    except ImportError:
        print('Ошибка в функции(name)')


def fairy_tales():
    """

    :return:
    """
    try:
        print('Находится в функции fairy_tales')
        # В моем списке есть такие сказки как
        play_music('speech synthesis/fairy_tales/В_моем_списке_есть_такие_сказки_как.mp3')
        # Три поросенка
        play_music('speech synthesis/fairy_tales/Три_поросенка.mp3')
        # Кукушка
        play_music('speech synthesis/fairy_tales/Кукушка.mp3')
        # Какую сказку хотите прослушать ?
        play_music('speech synthesis/fairy_tales/Какую_сказку_хотите_прослушать-.mp3')
        play_music('speech synthesis/sounds/blik.mp3')
        for tex in word_filter():
            if 'три поросёнка' in tex:
                fairy('три поросенка')
            elif 'кукушка' in tex:
                fairy('три поросенка')
    except ImportError:
        print('Ошибка в функции(fairy_tales)')


def fairy(text_far):
    if text_far == 'три поросенка':
        play_music('speech synthesis/fairy_tales/Чтоб поставить паузу скажите Пауза, Чтоб продолжить прослушивание '
                   'скажите Плей, Чтоб прервать.mp3')
        pygame.mixer.music.load('Audio_fairy_tales/tri-porosenka.mp3')
        pygame.mixer.music.play()
        while True:
            data = stream.read(8000)
            if (rec.AcceptWaveform(data)) and (len(data) > 0):
                answer = json.loads(rec.Result())
                if answer['text']:
                    if answer['text'] in cm.commands['pause']:
                        pygame.mixer.music.pause()
                    elif answer['text'] in cm.commands['продолжение']:
                        pygame.mixer.music.unpause()
                    elif answer['text'] in cm.commands['stop']:
                        pygame.mixer.music.stop()
                        main()

    elif text_far == 'кукушка':
        play_music('speech synthesis/fairy_tales/Чтоб поставить паузу скажите Пауза, Чтоб продолжить прослушивание '
                   'скажите Плей, Чтоб прервать.mp3')
        play_music('Audio_fairy_tales/кукушка.mp3')
        pygame.mixer.music.play()
        while True:
            data = stream.read(8000)
            if (rec.AcceptWaveform(data)) and (len(data) > 0):
                answer = json.loads(rec.Result())
                if answer['text']:
                    if answer['text'] in cm.commands['pause']:
                        pygame.mixer.music.pause()
                    elif answer['text'] in cm.commands['продолжение']:
                        pygame.mixer.music.unpause()
                    elif answer['text'] in cm.commands['stop']:
                        pygame.mixer.music.stop()
                        main()


def time_data():
    """

    :return:
    """
    print('находится в функции (time_data)')
    play_music('speech synthesis/data_time/В_данный_момент.mp3')

    # В данный момент
    try:
        dat = datetime.now()
        if dat.hour == 1:
            play_music('speech synthesis/data_time/1.mp3')
        elif dat.hour == 2:
            play_music('speech synthesis/data_time/2.mp3')
        elif dat.hour == 3:
            play_music('speech synthesis/data_time/3.mp3')
        elif dat.hour == 4:
            play_music('speech synthesis/data_time/4.mp3')
        elif dat.hour == 5:
            play_music('speech synthesis/data_time/5.mp3')
        elif dat.hour == 6:
            play_music('speech synthesis/data_time/6.mp3')
        elif dat.hour == 7:
            play_music('speech synthesis/data_time/7.mp3')
        elif dat.hour == 8:
            play_music('speech synthesis/data_time/8.mp3')
        elif dat.hour == 9:
            play_music('speech synthesis/data_time/9.mp3')
        elif dat.hour == 10:
            play_music('speech synthesis/data_time/10.mp3')
        elif dat.hour == 11:
            play_music('speech synthesis/data_time/11.mp3')
        elif dat.hour == 12:
            play_music('speech synthesis/data_time/12.mp3')
        elif dat.hour == 13:
            play_music('speech synthesis/data_time/13.mp3')
        elif dat.hour == 14:
            play_music('speech synthesis/data_time/14.mp3')
        elif dat.hour == 15:
            play_music('speech synthesis/data_time/15.mp3')
        elif dat.hour == 16:
            play_music('speech synthesis/data_time/16.mp3')
        elif dat.hour == 17:
            play_music('speech synthesis/data_time/17.mp3')
        elif dat.hour == 18:
            play_music('speech synthesis/data_time/18.mp3')
        elif dat.hour == 19:
            play_music('speech synthesis/data_time/19.mp3')
        elif dat.hour == 20:
            play_music('speech synthesis/data_time/20.mp3')
        elif dat.hour == 21:
            play_music('speech synthesis/data_time/21.mp3')
        elif dat.hour == 22:
            play_music('speech synthesis/data_time/22.mp3')
        elif dat.hour == 23:
            play_music('speech synthesis/data_time/23.mp3')
        elif dat.hour == 24:
            play_music('speech synthesis/data_time/24.mp3')
        main()
    except ImportError:
        print('Ошибка в функции (time_data)')

def time_of_day(text):
    """

    :param text:
    :return:
    """
    try:
        current_datetime = datetime.now()
        dat = current_datetime.hour
        if 'доброе утро' in text:
            if 5 < dat < 12:
                # доброе утро
                play_music('speech synthesis/wake_up_team/Доброе_утро.wav')
            if 12 < dat < 15:
                # добрый день
                play_music('speech synthesis/wake_up_team/Добрый-день.wav')
            if 15 < dat < 18:
                # добрый день
                play_music('speech synthesis/wake_up_team/Добрый-день.wav')
            if 18 < dat:
                # добрый вечер
                play_music('speech synthesis/wake_up_team/Добрый-вечер.wav')
            if dat == 0 or dat <= 5:
                # доброй ночи
                play_music('speech synthesis/wake_up_team/Доброй-ночи.wav')
        elif 'добрый день' in text:
            if 5 < dat < 12:
                # доброе утро
                play_music('speech synthesis/wake_up_team/Доброе_утро.wav')
            if 12 < dat < 15:
                # добрый день
                play_music('speech synthesis/wake_up_team/Добрый-день.wav')
            if 15 < dat < 18:
                # добрый день
                play_music('speech synthesis/wake_up_team/Добрый-день.wav')
            if 18 < dat:
                # добрый вечер
                play_music('speech synthesis/wake_up_team/Добрый-вечер.wav')
            if dat == 0 or dat <= 5:
                # доброй ночи
                play_music('speech synthesis/wake_up_team/Доброй-ночи.wav')
        elif 'добрый вечер' in text:
            if 5 < dat < 12:
                # доброе утро
                play_music('speech synthesis/wake_up_team/Доброе_утро.wav')
            if 12 < dat < 15:
                # добрый день
                play_music('speech synthesis/wake_up_team/Добрый-день.wav')
            if 15 < dat < 18:
                # добрый день
                play_music('speech synthesis/wake_up_team/Добрый-день.wav')
            if 18 < dat:
                # добрый вечер
                play_music('speech synthesis/wake_up_team/Добрый-вечер.wav')
            if dat == 0 or dat <= 5:
                # доброй ночи
                play_music('speech synthesis/wake_up_team/Доброй-ночи.wav')
        elif 'доброй ночи' in text:
            if 5 < dat < 12:
                # доброе утро
                play_music('speech synthesis/wake_up_team/Доброе_утро.wav')
            if 12 < dat < 15:
                # добрый день
                play_music('speech synthesis/wake_up_team/Добрый-день.wav')
            if 15 < dat < 18:
                # добрый день
                play_music('speech synthesis/wake_up_team/Добрый-день.wav')
            if 18 < dat:
                # добрый вечер
                play_music('speech synthesis/wake_up_team/Добрый-вечер.wav')
            if dat == 0 or dat <= 5:
                # доброй ночи
                play_music('speech synthesis/wake_up_team/Доброй-ночи.wav')
        main()
    except ImportError:
        print('Ошибка в функции(time_of_day)')


def muc(file_name):
    """
    Проигрывает аудиофайл и удаляет его после завершения.
    """
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(file_name)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)  # уменьшает нагрузку на CPU

        pygame.mixer.music.stop()        # ⛔ Остановить
        pygame.mixer.quit()              # 🧹 Освободить ресурс

        os.remove(file_name)             # ✅ Удалить после выгрузки
    except Exception as e:
        print(f'Ошибка в функции play_music: {e}')

def say(text):
    name_waw = 'output.wav' 
    tts = SileroTTS(
    language='ru',
    model_id='v4_ru',
    speaker='baya'  # 👈 допустимый голос
    )
    tts.tts(text, f'waw/{name_waw}')
    print(f"{text}✅")
    muc(f'waw/{name_waw}')



def vopros():
    print('находится в функции vopros')
    say('Слушаяю вас, Какой вопросс хотите задать?')
    while True:
        data = stream.read(8000)
        if (rec.AcceptWaveform(data)) and (len(data) > 0):
            answer = json.loads(rec.Result())
            if answer['text'] == 'выход':
                main()
            elif answer['text']:
                print(answer['text'])
                a = answer['text']
                print('думает....')
                response = g4f.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": f"{a}"}])
                print(response)
                print('закончила думать')
                say(response)
                main()

def em():
    play_music('em/В моем списке есть.wav')

    set_emotion('happy')
    play_music('em/Радость .wav')
    time.sleep(2)

    set_emotion('sad')
    play_music('em\Грусть.wav')
    time.sleep(2)

    set_emotion('angry')
    play_music('em\Злость.wav')
    time.sleep(2)

    set_emotion('neutral')
    play_music('em\Нейтральное лицо.wav')
    time.sleep(2)


    set_emotion('surprised')
    play_music('em\Удивление.wav')
    time.sleep(2)


    set_emotion('fearful')
    play_music('em\Страх.wav')
    time.sleep(2)


    set_emotion('disgusted')
    play_music('em\Отвращение.wav')
    time.sleep(2)
    main()

def main():
    """

    :return:
    """
    # чем могу быть полезна
    try:
        set_emotion('neutral')
        play_music('speech synthesis/sounds/blik.mp3')
        print('Находится в функции main')
        for text in word_filter():
            if text in cm.commands['как тебя звать']:
                set_emotion('happy')
                name()
            elif text in cm.commands['как дела']:
                haw_are_you()
            elif text in cm.commands['о боте']:
                about_the_robot()
            elif text in cm.commands['сказка']:
                fairy_tales()
            elif text in cm.commands['время']:
                time_data()
            elif text in cm.commands['включи_музыку']:
                music()
            elif text in cm.commands['вопрос']:
                vopros()
            elif text == 'эмоции':
                em()
            """else:
                # не совсем поняла вас повторите вопрос
                play_music('speech synthesis/main/Не_совсем_поняла_вас_повторите_вопрос_пожалуйста.wav')
                main()"""
    except ImportError:
        print('Ошибка в функции(main)')

def music():
    print('находится в функции(music)')
    q = 0
    files = ['5000-mp3.mp3', 'Alper_Eğri_Keep_Calm_Tiktok_Remix_UXuvQFD4Tjc_140.mp3', 'doc.mp3', 'Gasolina _rmx.mp3',
             'Gidayyat_HOVANNII_-_Sombrero_(musmore.com).mp3', 'Instasamka - Moneyken Love [BADAYTOFF TIKTOK EDIT].mp3',
             'Jengi - Bel mercy TikTok remix.mp3', 'lambada_bez_mata_-_lambada_bez_mata_(z2.fm).mp3',
             'marshmello-alone.mp3', 'Mi Gente.mp3', 'Mishlawi - All Night.mp3', 'Miyagi & Andy Panda - Тамада.mp3',
             'Move_Your_Body_.mp3', 'RaiM-Dvigatsya_Mikis_Remix__(mp3lav.com).mp3', 'Rozovoe_vino.mp3',
             'Skriptonit_-_Baby_Mama_Bez_mata_(Vuxo7.com).mp3', 'Smack That.mp3',
             'stromae-alors-on-danse-dubdogz-remix.mp3', 'timmy-turner.mp3', 'Toca Toca  T-Pain Low (DJ DIMVSH ).mp3',
             'Traag.mp3', 'Tyga & Азиятская Эстетика.mp3', 'ɢᴇᴛ ᴅᴏᴡɴ.mp3', 'Ганвест - На Рахате.mp3',
             'дискотека из 90.mp3', 'Клубняк _ ᴍɪx.mp3', 'лезгинка.mp3', 'мадина.mp3', 'медляк.mp3',
             'Мистер 718 – Скриптонит.mp3', 'Не ангиме_ ( без мата ) (320 kbps).mp3', 'пустите меня на танспол.mp3',
             'Скриптонит ft. 104, T-Fest - Мультибрендовый (Clean) (320 kbps).mp3',
             'Скриптонит_Танцуй_сама_izzamuzzic.mp3',
             'Скриптонит_х_ШИК_Пацан_х_Кеттик_Badaytoff_&_Daula_Partybreak_19.mp3']
    print(f'сейчас играет:{files[0]}')
    pygame.mixer.music.load(f'speech synthesis/музыка/{files[0]}')
    pygame.mixer.music.play()
    while True:
        data = stream.read(8000)
        if (rec.AcceptWaveform(data)) and (len(data) > 0):
            answer = json.loads(rec.Result())
            if answer['text']:
                print(answer['text'])
                if answer['text'] == 'дальше':
                    q = q + 1
                    print(f'{q} and {len(files)}')
                    if len(files) == q:
                        q = -1
                    else:
                        pygame.mixer.music.unload()
                        pygame.mixer.music.load(f'speech synthesis/музыка/{files[q]}')
                        pygame.mixer.music.play()
                        print(f'сейчас играет:{files[q]}')
                elif answer['text'] in cm.commands['pause']:
                    pygame.mixer.music.pause()
                elif answer['text'] in cm.commands['продолжение']:
                    pygame.mixer.music.unpause()
                elif answer['text'] in cm.commands['stop']:
                    pygame.mixer.music.stop()
                    main()
                if 'сто' in answer['text']:
                    pygame.mixer.music.set_volume(1.0)  # 100
                if 'девяносто' in answer['text']:
                    pygame.mixer.music.set_volume(0.9)  # 90
                if 'восемьдесят' in answer['text']:
                    pygame.mixer.music.set_volume(0.8)  # 80
                if 'семьдесят' in answer['text']:
                    pygame.mixer.music.set_volume(0.7)  # 70
                if 'шестьдесят' in answer['text']:
                    pygame.mixer.music.set_volume(0.6)  # 60
                if 'пятьдесят' in answer['text']:
                    pygame.mixer.music.set_volume(0.5)  # 50
                if 'сорок' in answer['text']:
                    pygame.mixer.music.set_volume(0.4)  # 40
                if 'тридцать' in answer['text']:
                    pygame.mixer.music.set_volume(0.3)  # 30
                if 'двадцать' in answer['text']:
                    pygame.mixer.music.set_volume(0.2)  # 20
                if 'десять' in answer['text']:
                    pygame.mixer.music.set_volume(0.1)  # 10
                if 'ноль' in answer['text']:
                    pygame.mixer.music.set_volume(0.0)  # 0


def wake_up_team():
    """

    :return:
    """
    try:
        set_emotion('neutral')
        print('Находится в функции ware_up_team')
        play_music('speech synthesis/sounds/blik.mp3')
        for text in word_filter():
            if 'привет' in text:
                # привет
                #play_music('speech synthesis/wake_up_team/Привет.wav')
                play_music('speech synthesis/wake_up_team/Здравствуйте.wav')
                break
            if 'здравствуйте' in text or 'здравствуй' in text:
                # здравствуйте
                play_music('speech synthesis/wake_up_team/Здравствуйте.wav')
                break
            if 'доброе утро' in text:
                print(123)
                time_of_day(text)
            if 'добрый день' in text:
                time_of_day(text)
            if 'добрый вечер' in text:
                time_of_day(text)
            if 'доброй ночи' in text:
                time_of_day(text)
            if 'салют' in text:
                # салют
                play_music('speech synthesis/wake_up_team/Салют.wav')
                break
            if 'хай' in text:
                # хай
                play_music('speech synthesis/wake_up_team/Хай_1.wav')
                break
            if 'глория' in text:
                # Слушаю
                play_music('speech synthesis/wake_up_team/Слушаю_1.wav')
                break
            else:
                wake_up_team()
            play_music('speech synthesis/main/чем_могу_быть_полезна.wav')
        main()
    except ImportError:
        print('Ошибка в функции(wake_up_time)')


if __name__ == '__main__':
    global_emotion_app = EmotionApp()

    # Запускаем логику ассистента в фоне
    threading.Thread(target=wake_up_team, daemon=True).start()

    # Запускаем GUI в главном потоке
    global_emotion_app.run()
