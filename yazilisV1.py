from tkinter import *
import random
import pygame

pygame.mixer.init()

root = Tk()
root.tk_setPalette("light blue")
root.attributes("-fullscreen", 1)


def okunus():
    o1 = ["Sıfır", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz", "On", "On bir", "On iki",
          "On üç", "On dört", "On beş", "On altı", "On yedi", "On sekiz", "On dokuz", "Yirmi"]

    birlik_1 = {"Sıfır": 0,
                "Bir": 1,
                "İki": 2,
                "Üç": 3,
                "Dört": 4,
                "Beş": 5,
                "Altı": 6,
                "Yedi": 7,
                "Sekiz": 8,
                "Dokuz": 9,
                "On": 10,
                "On bir": 11,
                "On iki": 12,
                "On üç": 13,
                "On dört": 14,
                "On beş": 15,
                "On altı": 16,
                "On yedi": 17,
                "On sekiz": 18,
                "On dokuz": 19,
                "Yirmi": 20}

    o2 = []
    o3 = []

    for t in random.sample(o1, 4):
        o2.append(t)

    o3.append(o2[0])

    soru = Label(text=str(o3[0]) + " sayısının yazılışı aşağıdakilerden hangisidir?                      ",
                 font="Times 24").place(relx=0.2, rely=0.1)

    def yaz_1():
        if s1 == o3[0]:
            pygame.mixer.music.load("alkis.mp3")
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.load("hata.mp3")
            pygame.mixer.music.play()

    for s1 in random.sample(o2, 1):
        but1 = Button(text=birlik_1[s1], command=yaz_1, height=1, width=15, fg="white", bg="red",
                      font="Times 20").place(relx=0.1, rely=0.3)

        o2.remove(s1)

    def yaz_2():
        if s2 == o3[0]:
            pygame.mixer.music.load("alkis.mp3")
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.load("hata.mp3")
            pygame.mixer.music.play()

    for s2 in random.sample(o2, 1):
        but2 = Button(text=birlik_1[s2], command=yaz_2, height=1, width=15, fg="white", bg="red",
                      font="Times 20").place(relx=0.1, rely=0.4)

        o2.remove(s2)

    def yaz_3():
        if s3 == o3[0]:
            pygame.mixer.music.load("alkis.mp3")
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.load("hata.mp3")
            pygame.mixer.music.play()

    for s3 in random.sample(o2, 1):
        but3 = Button(text=birlik_1[s3], command=yaz_3, height=1, width=15, fg="white", bg="red",
                      font="Times 20").place(relx=0.1, rely=0.5)

        o2.remove(s3)

    def yaz_4():
        if s4 == o3[0]:
            pygame.mixer.music.load("alkis.mp3")
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.load("hata.mp3")
            pygame.mixer.music.play()

    for s4 in random.sample(o2, 1):
        but4 = Button(text=birlik_1[s4], command=yaz_4, height=1, width=15, fg="white", bg="red",
                      font="Times 20").place(relx=0.1, rely=0.6)

        o2.remove(s4)


hazirla = Button(text='HAZIRLA', command=okunus, height=3, width=10, fg="white", bg="red",
                 font="Times 12").place(relx=0.1, rely=0.8)

buton = Button()
buton.config(text="ÇIKIŞ", command=root.destroy, height=3, width=10, fg="white", bg="red", font="Times 12")
buton.place(relx=0.8, rely=0.8)

root.mainloop()
