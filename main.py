# Import Modules
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from random import choice



# Main App Objects and Settings

app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Random word Maker")
main_window.resize(300, 200)



# Create all App Objects

title = QLabel("Something Temporary")


text1 = QLabel("?")
text2 = QLabel("?")
text3 = QLabel("?")


button1 = QPushButton("Press it")
button2 = QPushButton("Press it")
button3 = QPushButton("Press it")


my_words = ['hello', 'goodbye', 'app', 'test', 'python', 'sql', 'css', 'django']





# Design Part 

master_layout = QVBoxLayout()


row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()


row1.addWidget(title, alignment=Qt.AlignCenter)


row2.addWidget(text1, alignment=Qt.AlignCenter)
row2.addWidget(text2, alignment=Qt.AlignCenter)
row2.addWidget(text3, alignment=Qt.AlignCenter)


row3.addWidget(button1)
row3.addWidget(button2)
row3.addWidget(button3)



master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)


main_window.setLayout(master_layout)



# Functions Part

def random_word1():
    word = choice(my_words)
    text1.setText(word)



def random_word2():
    word = choice(my_words)
    text2.setText(word)



def random_word3():
    word = choice(my_words)
    text3.setText(word)


# Events

button1.clicked.connect(random_word1)
button2.clicked.connect(random_word2)
button3.clicked.connect(random_word3)





# Show/Run the app

main_window.show()
app.exec_()

