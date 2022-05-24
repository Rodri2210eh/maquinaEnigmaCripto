import tkinter
from tkinter import *

from maquinaEnigmaCripto.Enigma import enigmaM3


class Enigma:

    global temp
    global q
    global w
    global e
    global r
    global t
    global y
    global u
    global i
    global o
    global p
    global a
    global s
    global d
    global f
    global g
    global h
    global j
    global k
    global l
    global z
    global x
    global c
    global v
    global b
    global n
    global m
    fun : bool
    # Posicion inicial rotores
    inicio = ('A', 'B', 'C')
    # Orden rotores
    rotores = (4, 1, 3)
    # Reflectores
    reflector = 'B'
    # Posicion interna
    posInterna = ('A', 'A', 'A')
    # plugboard
    plugboard = [('A', 'M'), ('F', 'I'), ('N', 'V'), ('P', 'S'), ('T', 'U'), ('W', 'Z')]

    enigma : enigmaM3

    def __init__(self, root, fun):
        self.fun = fun
        self.msm = tkinter.StringVar()
        self.msm.set(" ")
        self.master = root
        self.label()
        self.botones()
        self.enigma = enigmaM3(self.rotores,self.reflector,self.inicio,self.posInterna,self.plugboard)





    def botones(self):
        global temp
        entry = tkinter.Entry(self.master, width=40 , textvariable=self.msm ).grid(column=10, row=2)

        button27 = tkinter.Button(self.master,
                                  text="Next Char",
                                  width=8,
                                  height=2,
                                  relief=tkinter.GROOVE,
                                  font="Courier  8 bold",
                                  background="gray",
                                  command=lambda: self.apagarValor(temp)
                                  ).grid(column=10, row=5)

        button1 = tkinter.Button(self.master,
                                 text="Q",
                                 width=8,
                                 height=2,
                                 relief=tkinter.GROOVE,
                                 font="Courier  8 bold",
                                 background="gray",
                                 command=lambda:self.verificacion('q')
                                 ).grid(column=0, row=5)

        button2 = tkinter.Button(self.master,
                                 text="W",
                                 width=8,
                                 height=2,
                                 relief=tkinter.GROOVE,
                                 font="Courier  8 bold",
                                 background="gray",
                                 command=lambda: self.verificacion('w')
                                 ).grid(column=1, row=5)

        button3 = tkinter.Button(self.master,
                                 text="E",
                                 width=8,
                                 height=2,
                                 relief=tkinter.GROOVE,
                                 font="Courier  8 bold",
                                 background="gray",
                                 command=lambda: self.verificacion('e')
                                 ).grid(column=2, row=5)

        button4 = tkinter.Button(self.master,
                                 text="R",
                                 width=8,
                                 height=2,
                                 relief=tkinter.GROOVE,
                                 font="Courier  8 bold",
                                 background="gray",
                                 command=lambda: self.verificacion('r')
                                 ).grid(column=3, row=5)

        button5 = tkinter.Button(self.master,
                                 text="T",
                                 width=8,
                                 height=2,
                                 relief=tkinter.GROOVE,
                                 font="Courier  8 bold",
                                 background="gray",
                                 command=lambda: self.verificacion('t')
                                 ).grid(column=4, row=5)

        button6 = tkinter.Button(self.master,
                                 text="Y",
                                 width=8,
                                 height=2,
                                 relief=tkinter.GROOVE,
                                 font="Courier  8 bold",
                                 background="gray",
                                 command=lambda: self.verificacion('y')
                                 ).grid(column=5, row=5)

        button7 = tkinter.Button(self.master,
                                 text="U",
                                 width=8,
                                 height=2,
                                 relief=tkinter.GROOVE,
                                 font="Courier  8 bold",
                                 background="gray",
                                 command=lambda: self.verificacion('u')
                                 ).grid(column=6, row=5)

        button8 = tkinter.Button(self.master,
                                 text="I",
                                 width=8,
                                 height=2,
                                 relief=tkinter.GROOVE,
                                 font="Courier  8 bold",
                                 background="gray",
                                 command=lambda: self.verificacion('i')
                                 ).grid(column=7, row=5)

        button9 = tkinter.Button(self.master,
                                 text="O",
                                 width=8,
                                 height=2,
                                 relief=tkinter.GROOVE,
                                 font="Courier  8 bold",
                                 background="gray",
                                 command=lambda: self.verificacion('o')
                                 ).grid(column=8, row=5)

        button10 = tkinter.Button(self.master,
                                 text="P",
                                 width=8,
                                 height=2,
                                 relief=tkinter.GROOVE,
                                 font="Courier  8 bold",
                                 background="gray",
                                 command=lambda: self.verificacion('p')
                                 ).grid(column=9, row=5)

        button11 = tkinter.Button(self.master,
                                 text="A",
                                 width=8,
                                 height=2,
                                 relief=tkinter.GROOVE,
                                 font="Courier  8 bold",
                                 background="gray",
                                 command=lambda: self.verificacion('a')
                                 ).grid(column=0, row=6)

        button12 = tkinter.Button(self.master,
                                 text="S",
                                 width=8,
                                 height=2,
                                 relief=tkinter.GROOVE,
                                 font="Courier  8 bold",
                                 background="gray",
                                 command=lambda: self.verificacion('s')
                                 ).grid(column=1, row=6)

        button13 = tkinter.Button(self.master,
                                 text="D",
                                 width=8,
                                 height=2,
                                 relief=tkinter.GROOVE,
                                 font="Courier  8 bold",
                                 background="gray",
                                 command=lambda: self.verificacion('d')
                                 ).grid(column=2, row=6)

        button14 = tkinter.Button(self.master,
                                 text="F",
                                 width=8,
                                 height=2,
                                 relief=tkinter.GROOVE,
                                 font="Courier  8 bold",
                                 background="gray",
                                 command=lambda: self.verificacion('f')
                                 ).grid(column=3, row=6)

        button15 = tkinter.Button(self.master,
                                 text="G",
                                 width=8,
                                 height=2,
                                 relief=tkinter.GROOVE,
                                 font="Courier  8 bold",
                                 background="gray",
                                 command=lambda: self.verificacion('g')
                                 ).grid(column=4, row=6)

        button16 = tkinter.Button(self.master,
                                 text="H",
                                 width=8,
                                 height=2,
                                 relief=tkinter.GROOVE,
                                 font="Courier  8 bold",
                                 background="gray",
                                 command=lambda: self.verificacion('h')
                                 ).grid(column=5, row=6)

        button17 = tkinter.Button(self.master,
                                 text="J",
                                 width=8,
                                 height=2,
                                 relief=tkinter.GROOVE,
                                 font="Courier  8 bold",
                                 background="gray",
                                 command=lambda: self.verificacion('j')
                                 ).grid(column=6, row=6)

        button18 = tkinter.Button(self.master,
                                 text="K",
                                 width=8,
                                 height=2,
                                 relief=tkinter.GROOVE,
                                 font="Courier  8 bold",
                                 background="gray",
                                 command=lambda: self.verificacion('k')
                                 ).grid(column=7, row=6)

        button19 = tkinter.Button(self.master,
                                 text="L",
                                 width=8,
                                 height=2,
                                 relief=tkinter.GROOVE,
                                 font="Courier  8 bold",
                                 background="gray",
                                 command=lambda: self.verificacion('l')
                                 ).grid(column=8, row=6)

        button20 = tkinter.Button(self.master,
                                 text="Z",
                                 width=8,
                                 height=2,
                                 relief=tkinter.GROOVE,
                                 font="Courier  8 bold",
                                 background="gray",
                                 command=lambda: self.verificacion('z')
                                 ).grid(column=0, row=7)

        button21 = tkinter.Button(self.master,
                                 text="X",
                                 width=8,
                                 height=2,
                                 relief=tkinter.GROOVE,
                                 font="Courier  8 bold",
                                 background="gray",
                                 command=lambda: self.verificacion('x')
                                 ).grid(column=1, row=7)

        button22 = tkinter.Button(self.master,
                                 text="C",
                                 width=8,
                                 height=2,
                                 relief=tkinter.GROOVE,
                                 font="Courier  8 bold",
                                 background="gray",
                                 command=lambda: self.verificacion('c')
                                 ).grid(column=2, row=7)

        button23 = tkinter.Button(self.master,
                                 text="V",
                                 width=8,
                                 height=2,
                                 relief=tkinter.GROOVE,
                                 font="Courier  8 bold",
                                 background="gray",
                                 command=lambda: self.verificacion('v')
                                 ).grid(column=3, row=7)

        button24 = tkinter.Button(self.master,
                                 text="B",
                                 width=8,
                                 height=2,
                                 relief=tkinter.GROOVE,
                                 font="Courier  8 bold",
                                 background="gray",
                                 command=lambda: self.verificacion('b')
                                 ).grid(column=4, row=7)

        button25 = tkinter.Button(self.master,
                                 text="N",
                                 width=8,
                                 height=2,
                                 relief=tkinter.GROOVE,
                                 font="Courier  8 bold",
                                 background="gray",
                                 command=lambda: self.verificacion('n')
                                 ).grid(column=5, row=7)

        button26 = tkinter.Button(self.master,
                                 text="M",
                                 width=8,
                                 height=2,
                                 relief=tkinter.GROOVE,
                                 font="Courier  8 bold",
                                 background="gray",
                                 command=lambda: self.verificacion('m')
                                 ).grid(column=6, row=7)





    def label(self):
        global w
        global e
        global r
        global t
        global y
        global u
        global i
        global o
        global p
        global a
        global s
        global d
        global f
        global g
        global h
        global j
        global k
        global l
        global z
        global x
        global c
        global v
        global b
        global n
        global m
        global q

        q = Label(self.master, text='Q')
        q.grid(column=0, row=2)
        w = Label(self.master, text='W')
        w.grid(column=1, row=2)
        e = Label(self.master, text='E')
        e.grid(column=2, row=2)
        r = Label(self.master, text='R')
        r.grid(column=3, row=2)
        t = Label(self.master, text='T')
        t.grid(column=4, row=2)
        y = Label(self.master, text='Y')
        y.grid(column=5, row=2)
        u = Label(self.master, text='U')
        u.grid(column=6, row=2)
        i = Label(self.master, text='I')
        i.grid(column=7, row=2)
        o = Label(self.master, text='O')
        o.grid(column=8, row=2)
        p = Label(self.master, text='P')
        p.grid(column=9, row=2)

        a = Label(self.master, text='A')
        a.grid(column=0, row=3)
        s = Label(self.master, text='S')
        s.grid(column=1, row=3)
        d = Label(self.master, text='D')
        d.grid(column=2, row=3)
        f = Label(self.master, text='F')
        f.grid(column=3, row=3)
        g = Label(self.master, text='G')
        g.grid(column=4, row=3)
        h = Label(self.master, text='H')
        h.grid(column=5, row=3)
        j = Label(self.master, text='J')
        j.grid(column=6, row=3)
        k = Label(self.master, text='K')
        k.grid(column=7, row=3)
        l = Label(self.master, text='L')
        l.grid(column=8, row=3)

        z = Label(self.master, text='Z')
        z.grid(column=0, row=4)
        x = Label(self.master, text='X')
        x.grid(column=1, row=4)
        c = Label(self.master, text='C')
        c.grid(column=2, row=4)
        v = Label(self.master, text='V')
        v.grid(column=3, row=4)
        b = Label(self.master, text='B')
        b.grid(column=4, row=4)
        n = Label(self.master, text='N')
        n.grid(column=5, row=4)
        m = Label(self.master, text='M')
        m.grid(column=6, row=4)



    def verificacion(self,x):
        global temp
        if self.fun:
            temp = self.encriptar(x)
            self.msm.set(self.msm.get()+temp)
            self.encenderValores(temp)


        else:
            temp = self.desencriptar(x)
            self.msm.set(self.msm.get() + temp)
            self.encenderValores(temp)




    def encenderValores(self, val):
        if val == 'q':
            global q
            q.config(fg='red')
        elif val == 'w':
            global w
            w.config(fg='red')
        elif val == 'e':
            global e
            e.config(fg='red')
        elif val == 'r':
            global r
            r.config(fg='red')
        elif val == 't':
            global t
            t.config(fg='red')
        elif val == 'y':
            global y
            y.config(fg='red')
        elif val == 'u':
            global u
            u.config(fg='red')
        elif val == 'i':
            global i
            i.config(fg='red')
        elif val == 'o':
            global o
            o.config(fg='red')
        elif val == 'p':
            global p
            p.config(fg='red')
        elif val == 'a':
            global a
            a.config(fg='red')
        elif val == 's':
            global s
            s.config(fg='red')
        elif val == 'd':
            global d
            d.config(fg='red')
        elif val == 'f':
            global f
            f.config(fg='red')
        elif val == 'g':
            global g
            g.config(fg='red')
        elif val == 'h':
            global h
            h.config(fg='red')
        elif val == 'j':
            global j
            j.config(fg='red')
        elif val == 'k':
            global k
            k.config(fg='red')
        elif val == 'l':
            global l
            l.config(fg='red')
        elif val == 'z':
            global z
            z.config(fg='red')
        elif val == 'x':
            global x
            x.config(fg='red')
        elif val == 'c':
            global c
            c.config(fg='red')
        elif val == 'v':
            global v
            v.config(fg='red')
        elif val == 'b':
            global b
            b.config(fg='red')
        elif val == 'n':
            global n
            n.config(fg='red')
        elif val == 'm':
            global m
            m.config(fg='red')



    def apagarValor(self, val):
        if val == 'q':
            global q
            q.config(fg='black')
        elif val == 'w':
            global w
            w.config(fg='black')
        elif val == 'e':
            global e
            e.config(fg='black')
        elif val == 'r':
            global r
            r.config(fg='black')
        elif val == 't':
            global t
            t.config(fg='black')
        elif val == 'y':
            global y
            y.config(fg='black')
        elif val == 'u':
            global u
            u.config(fg='black')
        elif val == 'i':
            global i
            i.config(fg='black')
        elif val == 'o':
            global o
            o.config(fg='black')
        elif val == 'p':
            global p
            p.config(fg='black')
        elif val == 'a':
            global a
            a.config(fg='black')
        elif val == 's':
            global s
            s.config(fg='black')
        elif val == 'd':
            global d
            d.config(fg='black')
        elif val == 'f':
            global f
            f.config(fg='black')
        elif val == 'g':
            global g
            g.config(fg='black')
        elif val == 'h':
            global h
            h.config(fg='black')
        elif val == 'j':
            global j
            j.config(fg='black')
        elif val == 'k':
            global k
            k.config(fg='black')
        elif val == 'l':
            global l
            l.config(fg='black')
        elif val == 'z':
            global z
            z.config(fg='black')
        elif val == 'x':
            global x
            x.config(fg='black')
        elif val == 'c':
            global c
            c.config(fg='black')
        elif val == 'v':
            global v
            v.config(fg='black')
        elif val == 'b':
            global b
            b.config(fg='black')
        elif val == 'n':
            global n
            n.config(fg='black')
        elif val == 'm':
            global m
            m.config(fg='black')


    def encriptar(self, x):
        temp = self.enigma.cifrar(x.upper())
        return temp.lower()

    def desencriptar(self, x):
        temp = self.enigma.descifrar(x.upper())
        return temp.lower()



def inicioGUI(bool,x):
    x.destroy()
    root = Tk()
    root.title('Maquina Enigma')
    root.geometry('1000x200')
    Enigma(root, bool)
    root.mainloop()

def menu():
    myWindow = Tk()
        # Establecer título
    myWindow.title('Menu de seleccion')
        # Crea dos botones
    b1 = Button(myWindow, text='Encriptar', command= lambda: inicioGUI(True,myWindow), font=('Helvetica 10 bold'), width=21, height=2)
    b1.grid(row=0, column=0, sticky=W, padx=5, pady=5)
    b2 = Button(myWindow, text='Desencriptar', command= lambda: inicioGUI(False, myWindow), font=('Helvetica 10 bold'), width=21, height=2)
    b2.grid(row=0, column=1, sticky=W, padx=5, pady=5)
    myWindow.mainloop()

menu()