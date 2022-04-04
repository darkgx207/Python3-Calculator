from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

mem = ''
mem_ = {'+/-': [], '*': [], '/': []}


class Janela(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uidata = uic.loadUi('./calculadora.ui', self)
        self.show()
        # ----------- Numbers ---------- #
        uidata.b0.clicked.connect(lambda: uidata.tela.display(memory(0)))
        uidata.b1.clicked.connect(lambda: uidata.tela.display(memory(1)))
        uidata.b2.clicked.connect(lambda: uidata.tela.display(memory(2)))
        uidata.b3.clicked.connect(lambda: uidata.tela.display(memory(3)))
        uidata.b4.clicked.connect(lambda: uidata.tela.display(memory(4)))
        uidata.b5.clicked.connect(lambda: uidata.tela.display(memory(5)))
        uidata.b6.clicked.connect(lambda: uidata.tela.display(memory(6)))
        uidata.b7.clicked.connect(lambda: uidata.tela.display(memory(7)))
        uidata.b8.clicked.connect(lambda: uidata.tela.display(memory(8)))
        uidata.b9.clicked.connect(lambda: uidata.tela.display(memory(9)))
        # --------------- Functions ----------------- #
        uidata.bc.clicked.connect(lambda: uidata.tela.display(cls(0)))
        uidata.bdel.clicked.connect(lambda: uidata.tela.display(delline()))
        # -------------- Operators ----------------- #
        uidata.bplus.clicked.connect(lambda: operator('+'))
        uidata.bless.clicked.connect(lambda: operator('-'))
        uidata.btimes.clicked.connect(lambda: operator('*'))
        uidata.bover.clicked.connect(lambda: operator('/'))
        uidata.beq.clicked.connect(lambda: operator('='))

        def memory(*args):
            global mem
            if len(mem) == 10:
                return mem
            mem = str(mem) + str(args[0])
            if mem[0] == '0' and len(mem) == 1:
                mem = mem + '.'
            return mem

        def cls(*args):
            global mem
            mem = str('')
            return 0

        def delline():
            global mem
            if len(mem) > 0:
                mem = mem[:-1]
                if mem == '':
                    return 0
            return mem

        # ------- Logic index for operations ----- #
        def operator(x):
            global mem_
            global mem

            if x == '+' or '-':
                if mem == '':
                    mem = x

                if mem != '':
                    mem.replace('+', '')
                    mem.replace('-', '')
                    mem_['+/-'].append(mem)
                    mem = x

                uidata.tela.display(mem)
                print(mem_)
            if x == '*':
                if len(mem) > 0:
                    tempMen = float(mem)
                    mem_['*'].append(tempMen)
                    uidata.tela.display(cls(0))
                    print(mem_)
            if x == '/':
                if len(mem) > 0:
                    tempMen = float(mem)
                    mem_['/'].append(tempMen)
                    uidata.tela.display(cls(0))
                    print(mem_)
            if x == '=':
                bEqual = sum(mem_['+'])
                mem = bEqual
                # ---- Result ----- #
                print(mem)


app = QApplication(sys.argv)
win = Janela()

app.exec_()