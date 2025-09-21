# 文件整理工具

自动按扩展名分类整理文件的工具。

## 文件说明

- `organizer.py`: 主程序文件

## 运行方法

```bash
cd file-organizer
python organizer.py
```

## 功能

- 按文件扩展名自动分类文件
- 支持多种文件类型（图片、文档、音频、视频等）
- 预览模式（不实际移动文件）
- 自动处理重名文件
- 安全确认机制

## 文件分类

- **图片**: .jpg, .jpeg, .png, .gif, .bmp, .svg, .webp
- **文档**: .pdf, .doc, .docx, .txt, .rtf, .odt
- **表格**: .xls, .xlsx, .csv, .ods
- **演示**: .ppt, .pptx, .odp
- **音频**: .mp3, .wav, .flac, .aac, .ogg
- **视频**: .mp4, .avi, .mkv, .mov, .wmv, .flv
- **压缩包**: .zip, .rar, .7z, .tar, .gz
- **代码**: .py, .js, .html, .css, .java, .cpp, .c
- **其他**: 未分类的文件

## 使用示例

```
请输入命令: preview /path/to/directory
=== 预览模式 ===
文件: image.jpg -> 分类: 图片
文件: document.pdf -> 分类: 文档
文件: script.py -> 分类: 代码

请输入命令: organize /path/to/directory
确认整理目录 '/path/to/directory' 吗? (y/n): y
创建目录: 图片
创建目录: 文档
移动文件: image.jpg -> 图片/image.jpg
移动文件: document.pdf -> 文档/document.pdf
```

## 注意事项

- 请在使用前备份重要文件
- 建议先使用预览模式查看整理结果
- 程序会自动处理重名文件（添加数字后缀）

## 学习要点

- 文件系统操作
- 路径处理
- 字典数据结构
- 异常处理
- 用户交互设计