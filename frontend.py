import os
import sys
import threading
import time
import zipfile
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel, QMessageBox, QWidget, QVBoxLayout
from PyQt5.QtCore import QSize, Qt, pyqtSignal, pyqtSlot, QTimer
from PyQt5.QtGui import QIcon, QPixmap, QMovie
import requests
import pandas as pd
import pickle

class UploadThread(QtCore.QThread):
    upload_started = pyqtSignal()
    upload_finished = pyqtSignal(bool)

    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path

    def run(self):
        self.upload_started.emit()
        # Load the model
        with open('model (1).pkl', 'rb') as f:
            rf_model = pickle.load(f)

        # Load and preprocess the data
        data = pd.read_csv(self.file_path)
        data = data.drop('Category', axis=1)
        data = data.drop(['pslist.nprocs64bit', 'handles.nport', 'handles.avg_handles_per_proc', 'ldrmodules.not_in_load_avg',
                          'ldrmodules.not_in_mem_avg', 'ldrmodules.not_in_init_avg', 'malfind.commitCharge', 'malfind.protection',
                          'malfind.uniqueInjections', 'svcscan.fs_drivers', 'callbacks.ngeneric'], axis=1)
        
        x_col = data.columns.to_list()
        x_col.pop(-1)
        x_data = data[x_col]
        
        # Normalize the data
        sc = StandardScaler()
        normed_data = pd.DataFrame(sc.fit_transform(x_data), columns=x_col)
        
        # Predict using the loaded model
        predictions = rf_model.predict(normed_data)
        analysis_result = predictions[0]

        if analysis_result == "Benign":
            self.upload_finished.emit(True)
        else:
            self.upload_finished.emit(False)

class BackendThread(QtCore.QThread):
    result_check = pyqtSignal()
    result_found = pyqtSignal(str)

    def run(self):
        self.result_check.emit()
        # Perform any necessary actions before checking the result

        # Mocking the result for demonstration
        result = "Benign"
        self.result_found.emit(result)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MALWARE FINDER")
        self.setMinimumSize(QtCore.QSize(600, 400))

        # Set the application icon
        app_icon = QIcon("gifs/icon.png")
        self.setWindowIcon(app_icon)

        self.bg_label = QLabel(self)
        self.bg_label.setScaledContents(True)
        self.bg_label.setGeometry(0, 0, self.width(), self.height())

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.gif_label = QLabel(self)
        self.gif = QMovie(self)

        self.upload_button = QPushButton("UPLOAD", self.central_widget)
        self.upload_button.setStyleSheet(
            "background-color: #F5C3EC;border-radius: 10px;font-family: Helvetica;font-size: 16px;"
        )
        self.upload_button.setFixedSize(200, 50)  # Set the button size here
        self.upload_button.clicked.connect(self.upload_file)

        self.upload_label = QLabel(self.central_widget)
        self.upload_label.setStyleSheet("color:white;font-size:25px")

        self.layout.addStretch(1)
        self.layout.addWidget(self.upload_button, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.upload_label, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.gif_label, alignment=Qt.AlignCenter)

        self.gif_path = "gifs/l-unscreen.gif"

    def resizeEvent(self, event):
        self.bg_label.setGeometry(0, 0, self.width(), self.height())
        self.gif_label.setGeometry(QtCore.QRect(240, 200, 120, 100))

    def set_background_image(self, file_path):
        try:
            pixmap = QPixmap(file_path)
            if pixmap.isNull():
                print("Failed to load the image:", file_path)
            else:
                scaled_pixmap = pixmap.scaled(self.bg_label.size(), QtCore.Qt.KeepAspectRatioByExpanding, QtCore.Qt.SmoothTransformation)
                self.bg_label.setPixmap(scaled_pixmap)
        except Exception as e:
            print("Error loading the image:", str(e))

    def upload_file(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)  
        file_dialog.setAcceptMode(QFileDialog.AcceptOpen)  
        file_dialog.setNameFilter("VMEM, MEM, DMP, and RAW files (*.vmem *.mem *.dmp *.raw *.png)")
        if file_dialog.exec_() == QFileDialog.Accepted:
            file_path = file_dialog.selectedFiles()[0]

            self.upload_label.setText("File uploading...")
            self.upload_label.adjustSize()

            self.upload_thread = UploadThread(file_path)
            self.upload_thread.upload_started.connect(self.start_gif)
            self.upload_thread.upload_finished.connect(self.upload_finished)
            self.upload_thread.start()

    @pyqtSlot(bool)
    def upload_finished(self, success):
        self.upload_thread = None

        if success:
            self.gif_label.hide()
            self.upload_label.setText("File uploaded successfully!")
            self.upload_label.adjustSize()

            QTimer.singleShot(2000, self.start_analyzing)
        else:
            self.gif_label.hide()
            self.upload_label.setText("Error uploading file")
            self.upload_label.adjustSize()

    def start_analyzing(self):
        self.gif_label.show()
        self.upload_label.setText("Analyzing   ")
        self.upload_label.adjustSize()

        self.backend_thread = BackendThread()
        self.backend_thread.result_check.connect(self.handle_result_check)
        self.backend_thread.result_found.connect(self.handle_result)
        self.backend_thread.start()

    def start_gif(self):
        self.gif = QMovie(self.gif_path)
        self.gif_label.setMovie(self.gif)
        self.gif_label.setAlignment(Qt.AlignCenter)
        self.gif.start()
        self.gif_label.show()

    def handle_result_check(self):
        pass

    def handle_result(self, result):
        self.gif_label.hide()
        self.upload_label.setText("")
        self.upload_label.adjustSize()
        if "Benign" in result:
            QMessageBox.information(self, "Result", "Your system is safe.")
        elif "Malware" in result:
            QMessageBox.warning(self, "Result", "Your system contains malware.")
        elif "" in result:
            QMessageBox.critical(self, "Error", "Error in analyzing the file.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.set_background_image("gifs/ff.png")
    window.show()
    sys.exit(app.exec_())
