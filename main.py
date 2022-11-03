import sys
from PyQt5 import uic, QtGui
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QApplication, QMainWindow
from StyleSheetRouter import StyleSheetRouter


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("style.ui", self)
        self.style_router = StyleSheetRouter(self, basic_key="basic", basic_filepath="StyleSheets/basic.qss")
        self.keyboard_clr_btn.clicked.connect(self.change_keyboard_clr)
        self.__initSounds()
        self.new_text = "Съешьте этих мягких французских булок, да выпейте же чаю"
        self.label.setText(self.create_insertion_string(self.new_text, ""))
        self.lineEdit.textChanged.connect(self.on_text_changed)
        print("done")

    def __initSounds(self):
        self.error_sound = QMediaPlayer()
        self.error_sound.setMedia(QMediaContent(QUrl.fromLocalFile("error.mp3")))


    def play_error_sound(self):
        self.error_sound.setVolume(self.volumeSlider.value())
        self.error_sound.play()

    def create_insertion_string(self, text, entered_text):
        insertion = ['<html><head/><body><p style="font-weight:600;"><span style="color: gray">',
                     '</span>',
                     '</p></body></html>']
        for part in insertion:
            text = text.replace(part, "", 1)

        outline = "{}".join(insertion).format(entered_text, text.replace(entered_text, "", 1))
        print(outline)

        return outline

    def on_text_changed(self):
        entered_text = self.lineEdit.text()
        if entered_text:
            if self.new_text[len(entered_text) - 1] == entered_text[-1]:
                self.label.setText(self.create_insertion_string(self.new_text, entered_text))
            else:
                self.play_error_sound()
                self.lineEdit.setText(entered_text[:-1])
        else:
            self.label.setText(self.create_insertion_string(self.new_text, ""))

    def change_keyboard_clr(self):
        if self.sender().property("isColored"):
            self.sender().setIcon(QtGui.QIcon("Images/drop.svg"))
            self.style_router.remove("colorful")
        else:
            self.sender().setIcon(QtGui.QIcon("Images/drop_red.svg"))
            self.style_router.add("colorful", "StyleSheets/colorful.qss")

        self.sender().setProperty("isColored", not self.sender().property("isColored"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
