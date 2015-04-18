__author__ = 'janet'

import tkinter
import time

# Hier wird der Splashscreen erstellt

class Splashscreen():

    def __init__(self, root, file, wait):
        """
        Werte initialisieren
        :param root: root
        :param file: Bild des Splashscreens
        :param wait: Wie lange soll es ausgefuehrt werden
        :return:
        """
        self.__root = root
        self.__file = file
        self.__wait = wait + time.clock()

    def __enter__(self):
        """
        Splashscreen ausgeben
        :return: Splashscreen mit Dauer der Ausfuehrung
        """

        # kl. Fenster verstecken
        self.__root.withdraw()

        # Komponenten erstellen
        window = tkinter.Toplevel(self.__root)
        canvas = tkinter.Canvas(window)
        splash = tkinter.PhotoImage(master=window, file=self.__file)

        # hoehe und breite des Splashscreens
        scrW = window.winfo_screenwidth()
        scrH = window.winfo_screenheight()

        # Bild groesse und breite
        imgW = splash.width()
        imgH = splash.height()

        # positionierung
        Xpos = (scrW - imgW) // 2
        Ypos = (scrH - imgH) // 2

        # canvas
        canvas.configure(width=imgW, height=imgH, highlightthickness=0)
        canvas.grid()

        # Splashscreen anzeigen
        canvas.create_image(imgW // 2, imgH // 2, image=splash)
        window.update()

        # Varibalen sichern
        self.__window = window
        self.__canvas = canvas
        self.__splash = splash

    def __exit__(self):
        """
        schliessen des Splashscreens
        :return:
        """

        # Kontrollieren ob die Zeit abgelaufen ist, in der er angezeigt wird
        now = time.clock()
        if now < self.__wait:
            time.sleep(self.__wait - now)
        del self.__splash
        self.__canvas.destroy()
        self.__window.destroy()

        # Sonnensystem wieder anklickbar machen
        self.__root.update_idletasks()



