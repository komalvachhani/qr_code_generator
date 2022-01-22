import os
import sys
import qrcode
from PIL.ImageQt import ImageQt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QStatusBar, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont, QPixmap, QImage
from PyQt5.QtCore import Qt

class QRCodeApp (QWidget):
    def __init__(self): # window setup
        super().__init__()
        self.setFixedSize(800,800)
        self.setWindowTitle('QR Code Generator')
        self.initUI()

    #function for the GUI
    def initUI(self):
        # font definition
        font = QFont('Open Sans', 16)

        # make box layouts for all the components
        mainLayout = QVBoxLayout()
        inputLayout = QHBoxLayout()
        buttonLayout = QHBoxLayout()
        imageLayout = QVBoxLayout()
        
        # fix image spacing
        imageLayout.addStretch()

        # widgets for the inputLayout
        label = QLabel('Enter Text: ')
        label.setFont(font)
        self.textInput = QLineEdit()
        self.textInput.setFont(font)
        
        # add label and textInput widgets to inputLayout
        inputLayout.addWidget(label)
        inputLayout.addWidget(self.textInput)

        # button widgets for buttonLayout + connections to each button function once clicked
        self.buttonGenerateQRCode = QPushButton('Generate QR Code')
        self.buttonGenerateQRCode.clicked.connect(self.generate_qr_code)

        self.buttonSaveQRCode = QPushButton('Save Image')
        self.buttonSaveQRCode.clicked.connect(self.save_qr_code)

        self.buttonClearFields = QPushButton('Clear Fields')
        self.buttonClearFields.clicked.connect(self.clear_fields)

        # add all 3 buttons to buttonLayout
        buttonLayout.addWidget(self.buttonGenerateQRCode)
        buttonLayout.addWidget(self.buttonSaveQRCode)
        buttonLayout.addWidget(self.buttonClearFields)

        # create the QR code image
        self.imageLabel = QLabel()
        self.imageLabel.setAlignment(Qt.AlignCenter)

        # add image widget to imageLayout
        imageLayout.addWidget(self.imageLabel)

        # add status bar at the bottom
        self.statusBar = QStatusBar()

        # add all the other layout containers to main layout
        mainLayout.addLayout(inputLayout)
        mainLayout.addLayout(buttonLayout)
        mainLayout.addLayout(imageLayout)
        mainLayout.addWidget(self.statusBar)
        
        # allows all of the components to display
        self.setLayout(mainLayout)

    # function to clear the fields
    def clear_fields (self):
        self.textInput.clear()
        self.imageLabel.clear()

    # function to generate the QR code
    def generate_qr_code (self):
        
        # receive input from the text input field
        text = self.textInput.text()

        # make and display the QR code
        qrCodeImage = qrcode.make(text)
        qr = ImageQt(qrCodeImage)
        pix = QPixmap.fromImage(qr)

        # send QR code to imageLabel
        self.imageLabel.setPixmap(pix)
    
    # function to save image as a file
    def save_qr_code (self):

        # set destination folder and file name
        current_directory = os.getcwd()
        file_name = self.textInput.text()

        if file_name:
            self.imageLabel.pixmap().save(os.path.join(current_directory, 'myqrcode.png'))
            self.statusBar.showMessage('QR Code is saved at {0}' .format(os.path.join(current_directory, 'myqrcode.png')))
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('QPushButton{Height: 40px; font-size: 20px}') # CSS for the button text

    demo = QRCodeApp()
    demo.show()

    sys.exit(app.exec_())