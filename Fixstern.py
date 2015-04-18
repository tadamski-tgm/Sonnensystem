__author__ = 'janet'

from OpenGL.GL import *
from OpenGL.GLU import *

# Hier wird der Fixstern erstellt

class Fixstern():

    def DrawGLScene_P(radius, rot, textur, light, x, y, z):
        """
        Erstellen der Sonne/Fixstern
        :param radius: Radius des Fixsterns
        :param rot: Variable fuer die Rotation
        :param textur: Textur fuer den FIxstern
        :param light: Varibale fuers Licht
        :param x: Koordinaten x
        :param y: Koordinaten y
        :param z: Koordinaten z
        :return: Fixstern
        """

        glLoadIdentity()                            # Screen neu laden
        glTranslatef(x, y, z)                       # Positionieren am Screen (x,y,z)
        glRotatef(rot[1], 0.0, 1.0, 0.0)            # Rotatation um Y-Achse

        glBindTexture(GL_TEXTURE_2D, textur)        # 2d Textur (x und y groesse)
        quadratic = gluNewQuadric()
        gluQuadricNormals(quadratic, GLU_SMOOTH)    # Erstellen von Smooth Normals
        gluQuadricTexture(quadratic, GL_TRUE)       # Erstellen von Texture Coords

        # Planet erstellen
        gluSphere(quadratic, radius, 32, 32)  # Parameter: Radius; Longitude; Latitude Segments

    def rotation(rot, x, y, z):
        """
        Rotation  der Sonne um sich selbst
        :param rot: Variable fuer Rotation
        :param x: Koordinaten x
        :param y: Koordinaten y
        :param z: Koordinaten z
        :return: Rotation
        """

        rot[1] = rot[1] + y  # Y achse
        return rot              # Rotation



