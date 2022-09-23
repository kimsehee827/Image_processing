
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *



def MyDisplay():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glRectf(-0.5, 0.5, 0.5, -0.5)
    glFlush()


def main():
    glutInit(sys.argv)
    glutCreateWindow('Hello World!')
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glutDisplayFunc(MyDisplay)
    glutMainLoop()


if __name__ == "__main__":
    main()

