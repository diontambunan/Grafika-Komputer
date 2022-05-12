# Nama        : Dion Sandy Ara Tambunan
# NIM         : 20051397056
# Kelas       : MI20B

#Gambar garis berikut menggunakan Algoritma Bresenham dengan titik awal A (10, 10) dan titik akhir B (21, 20)!

from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
#Mengakses konfigurasi interpreter pada saat runtime
import sys

def GarisDenganBresenham(x1, y1, x2, y2):
    #Menentukan delta X dan Y untuk mencari nilai pengubahan posisi
    x, y = x1, y1

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    gradien = dy/float(dx)

    #Jika gradien lebih dari 1
    if gradien > 1:
        dx, dy = dy, dx
        x, y   = y, x
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    p = 2 * dx - dy

    #Menentukan pixel yang akan digambar
    glVertex2f(x, y)

    #Perulangan
    for k in range(dx):
        if p > 0:
            y = y + 1 if y < y2 else y - 1
            p = p + 2 * (dy - dx)
        else:
            p = p + 2 * dy

        x = x + 1 if x < x2 else x - 1

        glVertex2f(x, y)

def TampilanGaris():
    #Membersihkan windows dengan latar warna hitam
    glClear(GL_COLOR_BUFFER_BIT)
    #Menentukan warna garis
    glColor(1.0,0.0,0.0)
    #Mulai menggambar garis dari titik
    glBegin(GL_LINES)
    #Besar titik awal dan akhir
    GarisDenganBresenham(10, 10, 21, 20)
    #Mengakhiri garis
    glEnd()
    #Menukar bagian belakang buffer menjadi layar
    glutSwapBuffers()

def main():
    #Menginisialisasi nilai-nilai yang ada pada library GLUT
    glutInit(sys.argv)
    #Menentukan penggunakan model pewarnaan RGB atau indeks warna untuk objek
    glutInitDisplayMode(GLUT_RGBA|GLUT_DOUBLE|GLUT_ALPHA|GLUT_DEPTH)
    #Menentukan ukuran window
    glutInitWindowSize(500, 500)
    #Menentukan posisi window
    glutInitWindowPosition(0,0)
    #Membuat window
    glutCreateWindow('Penerapan Garis dengan Algoritma Bresenham')
    glutDisplayFunc(TampilanGaris)
    glutIdleFunc(TampilanGaris)
    #Membersihkan latar dengan mode RGBA
    glClearColor(0.0,0.0,0.0,1.0)
    #Mengatur proyeksi hasil eksekusi dan mendefinisikan besarnya sistem koordinat
    gluOrtho2D(0.0, 50.0, 0.0, 50.0)
    #Melooping fungsi atau method main
    glutMainLoop()

main()