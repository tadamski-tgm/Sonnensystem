__author__ = 'janet'

from OpenGL.GL import *
from OpenGL.GLU import *

# Hier werden die Planeten erstellt (Erde, Mars)

class Planeten():

    def DrawGLScene_P(radius, rot, textur, light, x, y, z):
        """
        Planeten erstellen
        :param radius: groesse des Planeten
        :param rot: rotations Variable
        :param textur: Textur des Planeten
        :param light: Licht
        :param x: Koordinaten x
        :param y: Koordinaten y
        :param z: Koordinaten z
        :return: Planet
        """

        glLoadIdentity()                            # Screen neu laden
        glTranslatef(x, y, z)                       # Positionieren am Screen (x,y,z)
        glRotatef(rot[1], 0.0, 1.0, 0.0)            # Rotatation um Y-Achse
        glTranslatef(3.0, 0.0, 3.0)                 # neu Positionieren am Screen (x,y,z)

        glBindTexture(GL_TEXTURE_2D, textur)        # 2d texture (x and y size)
        quadratic = gluNewQuadric()
        gluQuadricNormals(quadratic, GLU_SMOOTH)    # Create Smooth Normals (NEW)
        gluQuadricTexture(quadratic, GL_TRUE)       # Create Texture Coords (NEW)

        # Planet erstellen
        gluSphere(quadratic, radius, 32, 32)        # Parameter: Radius; Longitude; Latitude Segments

    def rotation(rot, x, y, z):
        """
        Rotation des Planeten
        :param rot: rotations Variable
        :param x: Koordinaten x
        :param y: Koordinaten y
        :param z: Koordinaten z
        :return: Rotation
        """
        #Rotation um die Sonne
        rot[1] = rot[1] + y                         # Y achse
        return rot                                  # Rotation zurueckgeben



