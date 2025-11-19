from PyQt5 import QtWidgets, QtGui, QtCore

class DarkCalculator(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setStyleSheet("""
            QWidget {
                background-color: #232629;
                color: #EEE;
                font-size: 17px;
                font-family: "Segoe UI", "Arial";
            }
            QLineEdit {
                background-color: #18191b;
                border: 2px solid #444;
                border-radius: 8px;
                padding: 8px;
                color: #fff;
            }
            QPushButton {
                background-color: #353b40;
                border: 1px solid #2b2f33;
                border-radius: 8px;
                padding: 12px;
                min-width: 40px;
                min-height: 40px;
            }
            QPushButton:hover {
                background-color: #414952;
            }
            QPushButton:pressed {
                background-color: #222428;
            }
        """)

    def initUI(self):
        self.setWindowTitle("Karanlık Tema Hesap Makinesi")
        self.setFixedSize(320, 430)
        self.expression = ""
        mainLayout = QtWidgets.QVBoxLayout(self)
        mainLayout.setSpacing(15)
        mainLayout.setContentsMargins(20, 20, 20, 20)

        self.display = QtWidgets.QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(QtCore.Qt.AlignRight)
        self.display.setFixedHeight(48)
        mainLayout.addWidget(self.display)

        btns = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "C", "+"],
            ["(", ")", "=", ""]
        ]

        grid = QtWidgets.QGridLayout()
        for row, row_items in enumerate(btns):
            for col, item in enumerate(row_items):
                if item == "":
                    continue
                btn = QtWidgets.QPushButton(item)
                btn.clicked.connect(lambda checked, text=item: self.on_button(text))
                grid.addWidget(btn, row, col)
        mainLayout.addLayout(grid)

    def on_button(self, char):
        if char == "C":
            self.expression = ""
            self.display.setText("")
        elif char == "=":
            try:
                # Evaluate safely with allowed builtins only
                result = str(eval(self.expression, {"__builtins__": {}}))
                self.display.setText(result)
                self.expression = result
            except:
                self.display.setText("Hata")
                self.expression = ""
        else:
            self.expression += char
            self.display.setText(self.expression)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = DarkCalculator()
    window.show()
    sys.exit(app.exec_())
