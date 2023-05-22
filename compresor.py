from PIL import Image
import os
from tkinter import *
from tkinter import filedialog

downloadsFolder = filedialog.askdirectory()
picturesFolder = filedialog.askdirectory()

root = Tk()


if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)

        if extension in [".jpg", ".jpeg", ".png", ".xfc", ".gif", ".tiff", ".psd", ".bmp", ".eps", ".svg", ".ico", ".cdr"]:
            picture = Image.open(downloadsFolder + filename)
            picture.save(picturesFolder + "compressed_"+filename, optimize=True, quality=60)
            os.remove(downloadsFolder + filename)
            print(name + ": " + extension)

        if extension in [".mp3", ".ogg", ".wav", ".aiff", ".pcm", ".flac", ".alac", ".wma", ".aac", ".cda", ".rec"]:
            music_folder = "/SNOOPY/Music/"
            os.rename(downloadsFolder + filename, music_folder + filename)
            print(name + ": " + extension)

        if extension in [".odt", ".doc", ".docx", ".xls", ".xlsx", ".php"]:
            text_folder = "/SNOOPY/Music/"
            os.rename(downloadsFolder + filename, text_folder + filename)
            print(name + ": " + extension)

        if extension in [".bz2", ".tar", ".arj", ".iso", ".dmg"]:
            contenedores_de_compresion_folder = "/SNOOPY/Music/"
            os.rename(downloadsFolder + filename, contenedores_de_compresion_folder + filename)
            print(name + ": " + extension)

        if extension in [".svcd", ".wmm", ".mp4", ".mov", ".swf"]:
            video_folder = "/SNOOPY/Music/"
            os.rename(downloadsFolder + filename, video_folder + filename)
            print(name + ": " + extension)


root.mainloop()
