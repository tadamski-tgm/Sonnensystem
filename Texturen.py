__author__ = 'janet'

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL.Image import *      # fuer texturen

# Hier werden die Texturen erstellt

class Texturen():

    @staticmethod
    def loadTextures(bild):
        """
        Textur wird geladen
        :param bild: Pfad zu Bild
        :return: Textur
        """
        image = open(bild)

        # Textur
        ix = image.size[0]
        iy = image.size[1]
        image = image.tostring("raw", "RGBX", 0, -1)

        # Textur erstellen
        textur = glGenTextures(1)

        # BlindTexture
        glBindTexture(GL_TEXTURE_2D, textur)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_NEAREST)
        gluBuild2DMipmaps(GL_TEXTURE_2D, 3, ix, iy, GL_RGBA, GL_UNSIGNED_BYTE, image)

        return textur
