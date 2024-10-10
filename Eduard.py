from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QListWidget

app = QApplication([])
window = QWidget() #Створення вікна
window.setWindowTitle("Редактор фото")
window.resize(1000,800)

but_folder = QPushButton("Папка") 
list_img = QListWidget()
label_img = QLabel("Тут буде картинка")
but_left = QPushButton("Вліво")
but_right = QPushButton("Право")
but_mirrow = QPushButton("Дзеркально")
but_bluer = QPushButton("Різкість")
but_bw = QPushButton("Чорно-біле")

lineMain = QHBoxLayout()
lineV1 = QVBoxLayout()
lineV2 = QVBoxLayout()
lineH1 = QHBoxLayout()

lineV1.addWidget(but_folder)
lineV1.addWidget(list_img, 80)
lineMain.addLayout(lineV1)

lineV2.addWidget(label_img)
lineH1.addWidget(but_left)
lineH1.addWidget(but_right)
lineH1.addWidget(but_mirrow)
lineH1.addWidget(but_bluer)
lineH1.addWidget(but_bw)

lineV2.addLayout(lineH1)
lineMain.addLayout(lineV2,80)
window.setLayout(lineMain)

workdir = ''

def filter(files, extensions):
    result = []
    for filename in files:
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename)
        return result

window.show()
app.exec_()















