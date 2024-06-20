# SPIFFS 生成器

## 项目简介

SPIFFS 生成器是一款基于 PyQt 的图形化工具，用于生成 SPIFFS 文件系统镜像。该工具可以将指定目录中的文件打包成一个 SPIFFS 文件系统镜像，并保存为 `.bin` 格式文件。该工具特别适用于 ESP32 的开发。

## 功能特性

- 图形化用户界面，易于操作
- 支持自定义镜像大小、页面大小、块大小等参数
- 支持符号链接、魔数、大端模式等选项
- 输出 SPIFFS 镜像文件

## 目录结构

```
your_project/
│
├── spiffsgen_gui.py          # 主 GUI 程序
├── spiffsgen.py              # SPIFFS 生成逻辑
├── favicon.ico               # 应用程序图标
├── README.md                 # 使用说明文档
└── other_dependencies/       # 其他依赖项
```

## 安装步骤

### 克隆仓库

```bash
git clone
cd spiffsgen
```

### 创建并激活虚拟环境

```bash
python -m venv myenv
source myenv/bin/activate    # Linux 和 macOS
myenv\Scripts\activate       # Windows
```

### 安装依赖项

```bash
pip install -r requirements.txt
```

## 运行程序

### 直接运行

```bash
python spiffsgen_gui.py
```

### 打包为可执行文件

使用 PyInstaller 将程序打包为独立的可执行文件。

```bash
pyinstaller --onefile --noconsole --icon=favicon.ico spiffsgen_gui.py
```

打包完成后，可执行文件将位于 `dist/spiffsgen_gui.exe`。

## 使用指南

1. **启动工具**
   - 运行 `spiffsgen_gui.py` 或双击打包生成的 `.exe` 文件。

2. **设置参数**
   - 根据需要设置镜像大小、基目录、输出文件、页面大小、块大小、对象名称长度、元数据长度等参数。

3. **生成 SPIFFS 镜像**
   - 点击“生成”按钮，开始生成 SPIFFS 镜像文件。

4. **查看结果**
   - 生成成功后，将在指定位置生成 `.bin` 格式的 SPIFFS 镜像文件。

## 参数说明

- **镜像大小**：SPIFFS 镜像的大小（单位：字节）。
- **基目录**：包含要打包文件的目录。
- **输出文件**：生成的 SPIFFS 镜像文件路径（应为 `.bin` 格式）。
- **页面大小**：SPIFFS 文件系统的页面大小（单位：字节）。
- **块大小**：SPIFFS 文件系统的块大小（单位：字节）。
- **对象名称长度**：SPIFFS 文件系统中对象名称的最大长度（单位：字节）。
- **元数据长度**：SPIFFS 文件系统中文件元数据的长度（单位：字节）。
- **使用魔数**：是否在生成的 SPIFFS 镜像中使用魔数。
- **使用魔数长度**：是否根据位置生成不同的魔数。
- **跟随符号链接**：是否在创建镜像时包括符号链接。
- **大端模式**：是否使用大端字节序生成镜像。
- **对齐对象索引表**：是否对齐对象索引表。

## 开发信息

### 主要文件说明

- **spiffsgen_gui.py**：主 GUI 程序，使用 PyQt 构建图形界面并调用 SPIFFS 生成逻辑。
- **spiffsgen.py**：包含 SPIFFS 文件系统生成逻辑的核心代码。

### 依赖项

请确保安装以下 Python 库：

- PyQt5

可以通过以下命令安装：

```bash
pip install PyQt5
```

### 贡献

欢迎提出问题（Issues）和贡献代码（Pull Requests）。在提交代码之前，请确保遵循以下规范：

1. 编写清晰、简洁的代码。
2. 提供详细的提交说明。
3. 确保代码通过所有测试。

