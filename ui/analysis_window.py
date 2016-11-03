import sys
import os
from PySide.QtGui import *
from PySide.QtCore import *
from analysis_ui import Ui_Analysis
settings = QSettings('conf.ini', QSettings.IniFormat)

class AnalysisWindow(QMainWindow, Ui_Analysis):

    def __init__(self, parent = None):
        super(AnalysisWindow, self).__init__(parent)
        self.setupUi(self)
        self.startButton.clicked.connect(self.start_test)
        self.stopButton.clicked.connect(self.stop_test)
        self.filePickerButton2.clicked.connect(self.file_picker)
        self.filePickerButton.clicked.connect(self.file_picker2)
        self.checkBox.stateChanged.connect(self.set_rover)
        self.checkBox_2.stateChanged.connect(self.set_base)
        self.resolveAllButton.clicked.connect(self.resolve_all)
        self.fn_rover = ''
        self.fn_base = ''
        self.rov_fsize = 0
        self.base_fsize = 0

    def run_printer(self):
        pass

    def start_test(self):
        pass

    def stop_test(self):
        pass

    def file_picker(self):
        pass

    def set_progress(self):
        pass

    def get_current_loop(self):
        return self.test_control.loop

    def set_rover(self, value):
        if value:
            self.filePickerButton.setEnabled(True)
            self.roverPath.setEnabled(True)
        else:
            self.filePickerButton.setEnabled(False)
            self.roverPath.setEnabled(False)
            self.ready = False

    def set_base(self, value):
        if value:
            self.filePickerButton2.setEnabled(True)
            self.basePath.setEnabled(True)
        else:
            self.filePickerButton2.setEnabled(False)
            self.basePath.setEnabled(False)

    def file_picker(self):
        if settings.contains('analysis/basePath'):
            path = settings.value('analysis/basePath')
            print path
        else:
            path = os.getcwd()
        f = QFileDialog.getOpenFileName(self, 'Open raw measurement file', path, 'raw meas Files (*.rtcm3 *.raw)')
        self.fn_base = f[0]
        settings.setValue('analysis/basePath', os.path.dirname(self.fn_base))
        settings.sync()
        self.basePath.setText(self.fn_base)

    def file_picker2(self):
        if settings.contains('analysis/rovPath'):
            path = settings.value('analysis/rovPath')
            print path
        else:
            path = os.getcwd()
        f = QFileDialog.getOpenFileName(self, 'Open raw measurement file', path, 'raw meas Files (*.rtcm3 *.raw)')
        self.fn_rover = f[0]
        settings.setValue('analysis/rovPath', os.path.dirname(self.fn_rover))
        settings.sync()
        self.roverPath.setText(self.fn_rover)

    def resolve_all(self):
        pass

    def ready(self):
        if len(self.fn_rover) > 0 and self.roverPath.isEnabled():
            return True
        else:
            return False

    def cleanUp(self):
        for i in self.__dict__:
            item = self.__dict__[i]
            clean(item)


def clean(item):
    """Clean up the memory by closing and deleting the item if possible."""
    if isinstance(item, list) or isinstance(item, dict):
        for _ in range(len(item)):
            clean(list(item).pop())

    else:
        try:
            item.close()
        except (RuntimeError, AttributeError):
            pass

        try:
            item.deleteLater()
        except (RuntimeError, AttributeError):
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AnalysisWindow()
    window.show()
    sys.exit(app.exec_())
