__author__ = 'janet'

from OpenGL.GL import *

# Hier wird das Licht erstellt

class Licht():

    def setupLighting(self):
        """
        Licht setzen
        :return: Licht
        """

        # Variablen
        zeros = (0.15, 0.15, 0.15, 0.3)
        ones = (1.0, 1.0, 1.0, 0.3)
        half = (0.5, 0.5, 0.5, 0.5)

        # material Parameter fuer das Licht
        glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, zeros)
        glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, half)
        glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 15)

        # gibt das Licht zurueck (parameter)
        glLightfv(GL_LIGHT0, GL_AMBIENT, zeros)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, ones)
        glLightfv(GL_LIGHT0, GL_SPECULAR, half)

        # Position des Lichts
        glLightfv(GL_LIGHT0, GL_POSITION, (0,0,-8,1))

        # setzen des Lichts
        glEnable(GL_LIGHT0)
        glEnable(GL_LIGHTING)
        glColorMaterial(GL_FRONT_AND_BACK, GL_DIFFUSE)

        # Controls the Textur
        glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
        glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)

        # setzen
        glEnable(GL_COLOR_MATERIAL)
        glEnable(GL_NORMALIZE)
        glShadeModel(GL_SMOOTH)