if __name__ == '__build__':
   raise Exception

from Sonnensystem_3.Planeten import *
from Sonnensystem_3.Texturen import *
from Sonnensystem_3.Licht import *
from Sonnensystem_3.Splashscreen import *
from Sonnensystem_3.Fixstern import *
from Sonnensystem_3.Mond import *
from tkinter import *

class Screen():

    def __init__(self):
        """
        Konstruktor: initialisieren der Werte
        """

        self.rot_pl1 = [0, 1, 0]        # sonne
        self.rot_pl2 = [0, 0, 0]        # Erde
        self.rot_pl3 = [0, 0, 0]        # Mars
        self.rot_pl4 = [0, 0, 0]        # Mond

        # Werte zuweisen
        self.texture_num = 2            # fuer textur
        self.object = 0
        self.light = 0                  # fuer licht
        self.z = 50                     # fuer zoomen
        self.dreh = 1                   # fuer drehung + stoppen

        self.t = True                   # variable fuer Tasterturklick
        self.c = True                   # variable fuer Kamera
        self. h = True

        self.width = 1000
        self.height = 600

        self.intZaehler = 0

    def Menu(self):
        """
        Um das Menue anzeigen zu lassen (Steuerung etc)
        :return: Menu mit Tkinter anzeigen
        """
        root = Tk()
        text = Text(root)
        text.insert(INSERT, "\n>>HILFEFENSTER:\n"
                            "------------------------------------------------------------\n"
                            "|     Um fortzufahren, schliessen Sie dieses Fenster       |\n"
                            "|  Sie können die Hilfe mit der Taste 'H' wieder aufrufen  |\n"
                            "------------------------------------------------------------\n\n"
                            ">> TASTATUR:\n"
                            "'L' - Licht ein/aus\n"
                            "'T' - Textur ein/aus\n"
                            "'A' / 'S' - zum Steuern\n"
                            "'C' - Kameraansicht ändern\n"
                            "'P' - Stoppen der Animation\n"
                            "'Z' - Einzoomen\n"
                            "'U' - Auszoomen\n"
                            "'H' - Hilfe\n\n"
                            ">> MAUS:\n"
                            "Linke Maustaste - Licht ein/aus\n"
                            "Rechte Maustaste - Textur ein/aus")
        text.pack()
        root.mainloop()

    def InitGL(self, Width, Height):
        """
        Funktion setzt initial Parameter
        :param Width: Breite
        :param Height: Hoehe
        :return: Fenstergroesse
        """

        # Texturen laden
        self.quadratic_1 = Texturen.loadTextures("./Bilder/sonne.jpg")
        self.quadratic_2 = Texturen.loadTextures("./Bilder/erde.jpg")
        self.quadratic_3 = Texturen.loadTextures("./Bilder/mars.jpg")
        self.quadratic_4 = Texturen.loadTextures("./Bilder/mond.jpg")

        glEnable(GL_TEXTURE_2D)             # Texturen anzeigen
        glClearColor(0.0, 0.0, 0.0, 0.0)    # Hintergrundfarbe schwarz
        glClearDepth(1.0)                   # Loeschen des Depth Buffers
        glDepthFunc(GL_LESS)                # The Type Of Depth Test To Do
        glEnable(GL_DEPTH_TEST)             # Enables Depth Testing
        glShadeModel(GL_SMOOTH)             # Enables Smooth Color Shading

        glMatrixMode(GL_PROJECTION)         # Reset The Projection Matrix
        glLoadIdentity()

        Licht.setupLighting(self)           # Licht setzen

        self.Menu()                         # Menue aufrufen

        glMatrixMode(GL_MODELVIEW)

    def ReSizeGLScene(self, Width, Height):
        """
        Wenn die Groesse vom Fenster geaendert wird, sollen proportional bleiben
        :param Width: Breite
        :param Height: Hoehe
        :return: Seitenverhaeltnisse
        """

        # Das Fenster darf nicht zu klein sein
        if Height == 0:
            Height = 1

        self.width = Width
        self.height = Height

        # setzen des Viewports
        glViewport(0, 0, Width, Height)

    def DrawGLScene(self):
        """
        Funktion zum Erstellen der Planeten
        :return: Planeten
        """

        #Perspektive
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(self.z, float(self.width) / float(self.height), 0.1, 100.0)      # Perspektive erstellen

        # Kamera Perspektive
        if self.c is True:
            gluLookAt(0,0,1, 0,0,0, 0,1,0)      # Normalansicht (Seitlich)
        elif self.c is False:
            gluLookAt(0,20,0.5, 0,19,0, 0,1,0)  # Ansicht von Oben

        glMatrixMode(GL_MODELVIEW)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # buffer loeschen
        glLoadIdentity()                                    # Screen neu laden

        # Sonne aus Klasse Fixstern
        self.rot_pl1 = Fixstern.rotation(self.rot_pl1, 0, self.dreh*0.02, 0)                     # Rotation mit Achsen
        Fixstern.DrawGLScene_P(1.2, self.rot_pl1, self.quadratic_1, self.light, 0.6, 0, -10)       # Erstellen der Sonne

        # Erde aus Klasse Planeten
        self.rot_pl2 = Planeten.rotation(self.rot_pl2, 0, self.dreh*0.04, 0)                      # Rotation mit Achsen
        Planeten.DrawGLScene_P(0.3, self.rot_pl2, self.quadratic_2, self.light, 0.5, 0, -10)     # Erstellen des Planeten

         # Mond aus Klasse Mond
        self.rot_pl2 = Mond.rotation(self.rot_pl2, 0, self.dreh*0.04, 0)                          # Rotation mit Achsen
        Mond.DrawGLScene_P(0.08, self.rot_pl2, self.quadratic_4, self.light, 0.5, 0, -10)          # Erstellen des Mondes

        # Mars aus Klasse Planeten
        self.rot_pl3 = Planeten.rotation(self.rot_pl3, 0, self.dreh*0.04, 0)                     # Rotation mit Achsen
        Planeten.DrawGLScene_P(0.15, self.rot_pl3, self.quadratic_3, self.light, 2.1, 0, -10)   # Erstellen des Mondes

        glutSwapBuffers()  # zeichnen

    def keyPressed(self,key,x,y):
        """
        Tastertur bedienen
        :param key: Taste auf Tastatur
        :param x: Koordinaten x
        :param y: Koordinaten y
        :return: aufruf der Methoden bei Klick einer Taste
        """

        # Hilfe aufrufen
        if key == b'h':
            self.Menu()


        # Licht ein / aus
        if key == b'l':
            if self.t is True:
                glDisable(GL_LIGHTING)
                self.t = False
            elif self.t is False:
                glEnable(GL_LIGHTING)
                self.t = True

        # Textur ein / aus
        if key == b't':
            if self.t is True:
                glDisable(GL_TEXTURE_2D)
                self.t = False
            elif self.t is False:
                glEnable(GL_TEXTURE_2D)
                self.t = True

        # Kameraposition
        if key == b'c':
            if self.c is True:
                self.c = False
            elif self.c is False:
                self.c = True

        # Einzoomen
        if key == b'u':
            self.z = self.z + 0.5
            gluLookAt(0,0,self.z, 0,0,0, 0,1,0)
        elif self.z <= 15:
            self.z = 15

        # Auszoomen
        if key == b'z':
            self.z = self.z - 0.5
            gluLookAt(0,0,self.z, 0,0,0, 0,1,0)
        elif self.z >= 90:
            self.z = 90

        # Steuerung - Rotieren nach Rechts
        if key == b'a':
            Fixstern.rotation(self.rot_pl1,6.6, 0, 0)
            Planeten.rotation(self.rot_pl2, 0, 4.40, 0)
            Planeten.rotation(self.rot_pl3, 0, 2.20, 0)
            Planeten.rotation(self.rot_pl4, 0.0, 4.40, 0.0)
            self.dreh += 0.1

        # Steuerung - Rotieren nach Links
        elif key == b's':
            Planeten.rotation(self.rot_pl2, 0, -4.40, 0)
            Planeten.rotation(self.rot_pl3, 0, -2.20, 0)
            Planeten.rotation(self.rot_pl4, 0.0, -4.40, 0.0)
            self.dreh -= 0.1

        # Animation/Rotation stoppen
        elif key == b'p':
            Planeten.rotation(self.rot_pl2, 0, self.dreh, 0)
            Planeten.rotation(self.rot_pl3, 0, self.dreh, 0)
            Planeten.rotation(self.rot_pl4, 0.0, self.dreh, 0.0)
            self.dreh = 0

    def mouseClick(self,button,state,x,y):
        """
        Diese Function erkennt einen Mausklick am Bildschirm
        :param button: welche Taste auf der Maus wurde geklickt
        :param state: GLUT_DOWN
        :param x: Koordinaten
        :param y: Koordinaten
        :return: Aktion beim Klicken einer Maustaste
        """

         # Licht ein / aus
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
            if self.t is True:
                glDisable(GL_LIGHTING)
                self.t = False
            elif self.t is False:
                glEnable(GL_LIGHTING)
                self.t = True

        # Textur ein / aus
        if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
            if self.t is True:
                glDisable(GL_TEXTURE_2D)
                self.t = False
            elif self.t is False:
                glEnable(GL_TEXTURE_2D)
                self.t = True

    def main(self):
        """
        Main Methode - Hier werden die Functions aufgerufen
        """

        # Text der in der Console ausgegeben wird - Hilfestellung
        text = """
        >> TASTATUR:
        'L' - Licht ein/aus ODER LINKE MAUSTASTE
        'T' - Textur ein/aus ODER RECHTE MAUSTASTE
        'A' / 'S' - zum Steuern
        'C' - Kameraansicht ändern
        'P' - Stoppen der Animation
        'Z' - Einzoomen
        'U' - Auszoomen
        'H' - Hilfe aufrufen\n
        >> MAUS:
        Linke Maustaste - Licht ein/aus
        Rechte Maustaste - Textur ein/aus
        """

        print(text)                                             # Text/Anleitung ausgeben
        root = tkinter.Tk()
        sp = Splashscreen(root,'./Bilder/splash.gif',5)         # Splashscreen aufrufen - gif
        sp.__enter__()                                          # Splashscreen oeffnen
        sp.__exit__()                                           # Splashscreen schliessen
        root.iconify()                                          # kl. Fenster oeffnen
        root.deiconify()                                        # kl. Fenster schliessen
        root.destroy()

        glutInit(sys.argv)

        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)   # Select type of Display mode
        glutInitWindowSize(1000, 600)                               # Fenstergr 1000 x 600
        glutInitWindowPosition(50, 50)                              # the window starts at the upper left corner of the screen
        glutCreateWindow(b'Sonnensystem - Adamski & Weiss')         # Titel
        glutDisplayFunc(self.DrawGLScene)                           # Register the drawing function with glut
        glutMouseFunc(self.mouseClick)
        glutIdleFunc(self.DrawGLScene)                              # scene nochmal zeichnen
        glutReshapeFunc(self.ReSizeGLScene)                         # fenstergroesse aendern
        glutKeyboardFunc(self.keyPressed)			                # Tastertur verwenden
        self.InitGL(640, 480)                                       # fenster initialisieren
        glutMainLoop()                                              # Event starten

# Main Klasse aufrufen
if __name__ == "__main__":
    s = Screen()
    s.main()
