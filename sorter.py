import os
from PyQt6 import QtCore, QtWidgets, QtGui

class FileRenamerApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        layout = QtWidgets.QVBoxLayout()

        self.pathEdit = QtWidgets.QLineEdit(self)
        self.formatEdit = QtWidgets.QLineEdit(self)
        self.sortButton = QtWidgets.QPushButton('Sort it', self)
        self.resultLabel = QtWidgets.QLabel('', self)
        
        layout.addWidget(self.pathEdit)
        layout.addWidget(self.formatEdit)
        layout.addWidget(self.sortButton)
        layout.addWidget(self.resultLabel)

        self.setLayout(layout)

        self.sortButton.clicked.connect(self.sortFiles)

    def sortFiles(self):
        folder_path = self.pathEdit.text()
        file_format = self.formatEdit.text()
        
        try:
            file_list = [file for file in os.listdir(folder_path) if file.endswith(file_format)]
            num_files = len(file_list)
            self.resultLabel.setText(f"Number of files: {num_files}")

            for i, file_name in enumerate(file_list, start=1):
                new_file_name = f"{i}{file_format}"
                os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))
                print(f"File {file_name} to {new_file_name} renamed.")
            
            self.resultLabel.setText(f"All files have been renamed successfully:).")
        
        except Exception as e:
            self.resultLabel.setText(f"An error occurred:(: \n https://github.com/Ammaqouliqp/goodapps/blob/main/sorter.py ")

def main():
    app = QtWidgets.QApplication([])
    window = FileRenamerApp()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
