# ESP32 SPIFFS 生成器 / ESP32 SPIFFS Generator

## 项目简介 / Project Introduction

SPIFFS 生成器是一款基于 PyQt 的图形化工具，用于生成 SPIFFS 文件系统镜像。该工具可以将指定目录中的文件打包成一个 SPIFFS 文件系统镜像，并保存为 `.bin` 格式文件。该工具特别适用于 ESP32 的开发。

SPIFFS Generator is a graphical tool based on PyQt for generating SPIFFS file system images. This tool can package files from a specified directory into a SPIFFS file system image and save it as a `.bin` file. It is particularly useful for ESP32 development.

## 功能特性 / Features

- 图形化用户界面，易于操作
- 支持自定义镜像大小、页面大小、块大小等参数
- 支持符号链接、魔数、大端模式等选项
- 输出 SPIFFS 镜像文件

- Graphical user interface, easy to operate
- Support for custom image size, page size, block size, and other parameters
- Support for symbolic links, magic numbers, big-endian mode, etc.
- Output SPIFFS image file

## 目录结构 / Directory Structure

```
your_project/
│
├── spiffsgen_gui.py          # 主 GUI 程序 / Main GUI program
├── spiffsgen.py              # SPIFFS 生成逻辑 / SPIFFS generation logic
├── favicon.ico               # 应用程序图标 / Application icon
├── README.md                 # 使用说明文档 / Documentation
└── other_dependencies/       # 其他依赖项 / Other dependencies
```

## 安装步骤 / Installation Steps

### 克隆仓库 / Clone the Repository

```bash
git clone 
cd spiffsgen
```

### 创建并激活虚拟环境 / Create and Activate Virtual Environment

```bash
python -m venv myenv
source myenv/bin/activate    # Linux 和 macOS / Linux and macOS
myenv\Scripts\activate       # Windows
```

### 安装依赖项 / Install Dependencies

```bash
pip install -r requirements.txt
```

## 运行程序 / Run the Program

### 直接运行 / Run Directly

```bash
python spiffsgen_gui.py
```

### 打包为可执行文件 / Package as Executable

使用 PyInstaller 将程序打包为独立的可执行文件。 Use PyInstaller to package the program as a standalone executable.

```bash
pyinstaller --onefile --noconsole --icon=favicon.ico spiffsgen_gui.py
```

打包完成后，可执行文件将位于 `dist/spiffsgen_gui.exe`。 After packaging, the executable will be located in `dist/spiffsgen_gui.exe`.

## 使用指南 / Usage Guide

1. **启动工具 / Start the Tool**
   - 运行 `spiffsgen_gui.py` 或双击打包生成的 `.exe` 文件。
   - Run `spiffsgen_gui.py` or double-click the generated `.exe` file.

2. **设置参数 / Set Parameters**
   - 根据需要设置镜像大小、基目录、输出文件、页面大小、块大小、对象名称长度、元数据长度等参数。
   - Set the image size, base directory, output file, page size, block size, object name length, metadata length, and other parameters as needed.

3. **生成 SPIFFS 镜像 / Generate SPIFFS Image**
   - 点击“生成”按钮，开始生成 SPIFFS 镜像文件。
   - Click the "Generate" button to start generating the SPIFFS image file.

4. **查看结果 / View Results**
   - 生成成功后，将在指定位置生成 `.bin` 格式的 SPIFFS 镜像文件。
   - After successful generation, a `.bin` format SPIFFS image file will be created at the specified location.

## 参数说明 / Parameter Description

- **镜像大小 / Image Size**：SPIFFS 镜像的大小（单位：字节）。/ Size of the SPIFFS image (in bytes).
- **基目录 / Base Directory**：包含要打包文件的目录。/ Directory containing files to be packaged.
- **输出文件 / Output File**：生成的 SPIFFS 镜像文件路径（应为 `.bin` 格式）。/ Path of the generated SPIFFS image file (should be in `.bin` format).
- **页面大小 / Page Size**：SPIFFS 文件系统的页面大小（单位：字节）。/ Page size of the SPIFFS file system (in bytes).
- **块大小 / Block Size**：SPIFFS 文件系统的块大小（单位：字节）。/ Block size of the SPIFFS file system (in bytes).
- **对象名称长度 / Object Name Length**：SPIFFS 文件系统中对象名称的最大长度（单位：字节）。/ Maximum length of object names in the SPIFFS file system (in bytes).
- **元数据长度 / Metadata Length**：SPIFFS 文件系统中文件元数据的长度（单位：字节）。/ Length of file metadata in the SPIFFS file system (in bytes).
- **使用魔数 / Use Magic Number**：是否在生成的 SPIFFS 镜像中使用魔数。/ Whether to use magic numbers in the generated SPIFFS image.
- **使用魔数长度 / Use Magic Length**：是否根据位置生成不同的魔数。/ Whether to generate different magic numbers based on position.
- **跟随符号链接 / Follow Symbolic Links**：是否在创建镜像时包括符号链接。/ Whether to include symbolic links when creating the image.
- **大端模式 / Big-Endian Mode**：是否使用大端字节序生成镜像。/ Whether to generate the image using big-endian byte order.
- **对齐对象索引表 / Align Object Index Tables**：是否对齐对象索引表。/ Whether to align object index tables.

## 开发信息 / Development Information

### 主要文件说明 / Main Files

- **spiffsgen_gui.py**：主 GUI 程序，使用 PyQt 构建图形界面并调用 SPIFFS 生成逻辑。/ Main GUI program, built with PyQt, calling the SPIFFS generation logic.
- **spiffsgen.py**：包含 SPIFFS 文件系统生成逻辑的核心代码。/ Core code containing the SPIFFS file system generation logic.

### 依赖项 / Dependencies

请确保安装以下 Python 库： / Please ensure the following Python libraries are installed:

- PyQt5

可以通过以下命令安装： / Can be installed with the following command:

```bash
pip install PyQt5
```

### 贡献 / Contribution

欢迎提出问题（Issues）和贡献代码（Pull Requests）。在提交代码之前，请确保遵循以下规范：

Issues and pull requests are welcome. Before submitting code, please ensure the following:

1. 编写清晰、简洁的代码。/ Write clear and concise code.
2. 提供详细的提交说明。/ Provide detailed commit messages.
3. 确保代码通过所有测试。/ Ensure all tests pass.
