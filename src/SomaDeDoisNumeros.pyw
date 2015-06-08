"""
*
* PYSIDE :: PySide is licensed under the LGPL version 2.1 license (https://github.com/PySide/PySide).
* 
"""

from PySide.QtGui import QApplication
from PySide.QtGui import QMainWindow
from PySide.QtGui import QPushButton
from PySide.QtGui import QTextEdit
from PySide.QtGui import QLineEdit
import sys

class SomaDeDoisNumeros(QMainWindow):
    def __init__(self):
        super (SomaDeDoisNumeros, self).__init__()

        self.num1 = QLineEdit(self)
        self.num1.move(10,10)
        
        self.num2 = QLineEdit(self)
        self.num2.move(150,10)
        
        self.botao = QPushButton('Somar', self)
        self.botao.move(80,60)
        self.botao.clicked.connect(self.somar)
        
        self.resultado = QLineEdit(self)
        self.resultado.move(80,110)
        
        self.setGeometry(500,200,260,180)
        self.setWindowTitle('SOMAR')
        
        self.show()

    def somar(self):
        try:
            soma = int(self.num1.text()) + int(self.num2.text())
            self.resultado.setText(str(soma))
        except:
            self.resultado.setText('Deixe Disso!')

if __name__ == '__main__':
    aplicacao = QApplication(sys.argv)
    soma = SomaDeDoisNumeros()
    sys.exit(aplicacao.exec_())
