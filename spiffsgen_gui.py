#!/usr/bin/env python

import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFileDialog, QCheckBox, QMessageBox
from spiffsgen import SpiffsBuildConfig, SpiffsFS, SPIFFS_PAGE_IX_LEN, SPIFFS_BLOCK_IX_LEN, SPIFFS_OBJ_ID_LEN, SPIFFS_SPAN_IX_LEN

class SpiffsGeneratorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.imageSizeLabel = QLabel('镜像大小（字节）:')
        self.imageSizeInput = QLineEdit(self)
        self.imageSizeInput.setText('983040')  # 设置默认值为 983040 字节
        layout.addWidget(self.imageSizeLabel)
        layout.addWidget(self.imageSizeInput)

        self.baseDirLabel = QLabel('基目录:')
        self.baseDirInput = QLineEdit(self)
        self.baseDirButton = QPushButton('浏览', self)
        self.baseDirButton.clicked.connect(self.selectBaseDir)
        layout.addWidget(self.baseDirLabel)
        layout.addWidget(self.baseDirInput)
        layout.addWidget(self.baseDirButton)

        self.outputFileLabel = QLabel('输出文件:')
        self.outputFileInput = QLineEdit(self)
        self.outputFileButton = QPushButton('浏览', self)
        self.outputFileButton.clicked.connect(self.selectOutputFile)
        layout.addWidget(self.outputFileLabel)
        layout.addWidget(self.outputFileInput)
        layout.addWidget(self.outputFileButton)

        self.pageSizeLabel = QLabel('页面大小（字节）:')
        self.pageSizeInput = QLineEdit(self)
        self.pageSizeInput.setText('256')
        layout.addWidget(self.pageSizeLabel)
        layout.addWidget(self.pageSizeInput)

        self.blockSizeLabel = QLabel('块大小（字节）:')
        self.blockSizeInput = QLineEdit(self)
        self.blockSizeInput.setText('4096')
        layout.addWidget(self.blockSizeLabel)
        layout.addWidget(self.blockSizeInput)

        self.objNameLenLabel = QLabel('对象名称长度:')
        self.objNameLenInput = QLineEdit(self)
        self.objNameLenInput.setText('32')
        layout.addWidget(self.objNameLenLabel)
        layout.addWidget(self.objNameLenInput)

        self.metaLenLabel = QLabel('元数据长度:')
        self.metaLenInput = QLineEdit(self)
        self.metaLenInput.setText('4')
        layout.addWidget(self.metaLenLabel)
        layout.addWidget(self.metaLenInput)

        self.useMagicCheckBox = QCheckBox('使用魔数', self)
        self.useMagicCheckBox.setChecked(True)
        layout.addWidget(self.useMagicCheckBox)

        self.useMagicLenCheckBox = QCheckBox('使用魔数长度', self)
        self.useMagicLenCheckBox.setChecked(True)
        layout.addWidget(self.useMagicLenCheckBox)

        self.followSymlinksCheckBox = QCheckBox('跟随符号链接', self)
        layout.addWidget(self.followSymlinksCheckBox)

        self.bigEndianCheckBox = QCheckBox('大端模式', self)
        layout.addWidget(self.bigEndianCheckBox)

        self.alignedObjIxTablesCheckBox = QCheckBox('对齐对象索引表', self)
        layout.addWidget(self.alignedObjIxTablesCheckBox)

        self.generateButton = QPushButton('生成', self)
        self.generateButton.clicked.connect(self.generateSpiffs)
        layout.addWidget(self.generateButton)

        self.setLayout(layout)
        self.setWindowTitle('SPIFFS 生成器')
        self.show()

    def selectBaseDir(self):
        dir = QFileDialog.getExistingDirectory(self, '选择基目录')
        if dir:
            self.baseDirInput.setText(dir)

    def selectOutputFile(self):
        file, _ = QFileDialog.getSaveFileName(self, '选择输出文件', filter='SPIFFS 镜像 (*.bin);;所有文件 (*)')
        if file:
            self.outputFileInput.setText(file)

    def generateSpiffs(self):
        imageSize = self.imageSizeInput.text()
        baseDir = self.baseDirInput.text()
        outputFile = self.outputFileInput.text()
        pageSize = int(self.pageSizeInput.text())
        blockSize = int(self.blockSizeInput.text())
        objNameLen = int(self.objNameLenInput.text())
        metaLen = int(self.metaLenInput.text())
        useMagic = self.useMagicCheckBox.isChecked()
        useMagicLen = self.useMagicLenCheckBox.isChecked()
        followSymlinks = self.followSymlinksCheckBox.isChecked()
        bigEndian = self.bigEndianCheckBox.isChecked()
        alignedObjIxTables = self.alignedObjIxTablesCheckBox.isChecked()

        if not os.path.exists(baseDir):
            QMessageBox.critical(self, '错误', '基目录不存在。')
            return

        try:
            with open(outputFile, 'wb') as image_file:
                image_size = int(imageSize, 0)
                spiffs_build_default = SpiffsBuildConfig(pageSize, SPIFFS_PAGE_IX_LEN,
                                                         blockSize, SPIFFS_BLOCK_IX_LEN, metaLen,
                                                         objNameLen, SPIFFS_OBJ_ID_LEN, SPIFFS_SPAN_IX_LEN,
                                                         True, True, 'big' if bigEndian else 'little',
                                                         useMagic, useMagicLen, alignedObjIxTables)

                spiffs = SpiffsFS(image_size, spiffs_build_default)

                for root, dirs, files in os.walk(baseDir, followlinks=followSymlinks):
                    for f in files:
                        full_path = os.path.join(root, f)
                        spiffs.create_file('/' + os.path.relpath(full_path, baseDir).replace('\\', '/'), full_path)

                image = spiffs.to_binary()
                image_file.write(image)

            QMessageBox.information(self, '成功', 'SPIFFS 镜像生成成功。')
        except Exception as e:
            QMessageBox.critical(self, '错误', str(e))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SpiffsGeneratorApp()
    sys.exit(app.exec_())
