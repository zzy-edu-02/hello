#!/usr/bin/env python3
"""
文件整理工具
按照文件扩展名自动整理文件到不同目录
"""

import os
import shutil
from pathlib import Path

class FileOrganizer:
    def __init__(self):
        # 定义文件类型分类
        self.file_categories = {
            '图片': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'],
            '文档': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt'],
            '表格': ['.xls', '.xlsx', '.csv', '.ods'],
            '演示': ['.ppt', '.pptx', '.odp'],
            '音频': ['.mp3', '.wav', '.flac', '.aac', '.ogg'],
            '视频': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv'],
            '压缩包': ['.zip', '.rar', '.7z', '.tar', '.gz'],
            '代码': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c'],
            '其他': []  # 默认分类
        }
    
    def get_file_category(self, file_extension):
        """根据文件扩展名获取分类"""
        file_extension = file_extension.lower()
        for category, extensions in self.file_categories.items():
            if file_extension in extensions:
                return category
        return '其他'
    
    def organize_directory(self, directory_path, create_folders=True):
        """整理指定目录中的文件"""
        directory = Path(directory_path)
        
        if not directory.exists():
            print(f"错误：目录 {directory_path} 不存在")
            return
        
        print(f"开始整理目录: {directory_path}")
        
        # 统计信息
        moved_files = 0
        created_folders = []
        
        # 遍历目录中的所有文件
        for file_path in directory.iterdir():
            if file_path.is_file():
                # 获取文件扩展名和分类
                file_extension = file_path.suffix
                category = self.get_file_category(file_extension)
                
                # 创建分类目录
                category_dir = directory / category
                if create_folders and not category_dir.exists():
                    category_dir.mkdir()
                    created_folders.append(category)
                    print(f"创建目录: {category}")
                
                # 移动文件
                if create_folders:
                    try:
                        new_path = category_dir / file_path.name
                        # 如果目标文件已存在，添加数字后缀
                        counter = 1
                        while new_path.exists():
                            name_part = file_path.stem
                            extension_part = file_path.suffix
                            new_name = f"{name_part}_{counter}{extension_part}"
                            new_path = category_dir / new_name
                            counter += 1
                        
                        shutil.move(str(file_path), str(new_path))
                        print(f"移动文件: {file_path.name} -> {category}/{new_path.name}")
                        moved_files += 1
                    except Exception as e:
                        print(f"移动文件失败 {file_path.name}: {e}")
                else:
                    print(f"文件: {file_path.name} -> 分类: {category}")
        
        print(f"\n整理完成！")
        print(f"移动文件数: {moved_files}")
        if created_folders:
            print(f"创建目录数: {len(created_folders)}")
    
    def preview_organization(self, directory_path):
        """预览整理结果，不实际移动文件"""
        print("=== 预览模式 ===")
        self.organize_directory(directory_path, create_folders=False)

def main():
    """主函数"""
    organizer = FileOrganizer()
    
    print("=== 文件整理工具 ===")
    print("功能:")
    print("1. organize <目录路径> - 整理文件")
    print("2. preview <目录路径> - 预览整理结果")
    print("3. show-categories - 显示文件分类")
    print("4. quit - 退出程序")
    
    while True:
        try:
            command = input("\n请输入命令: ").strip().split(' ', 1)
            action = command[0].lower()
            
            if action == 'quit':
                print("再见！")
                break
            
            elif action == 'organize' and len(command) > 1:
                directory_path = command[1]
                confirm = input(f"确认整理目录 '{directory_path}' 吗? (y/n): ")
                if confirm.lower() == 'y':
                    organizer.organize_directory(directory_path)
                else:
                    print("操作已取消")
            
            elif action == 'preview' and len(command) > 1:
                directory_path = command[1]
                organizer.preview_organization(directory_path)
            
            elif action == 'show-categories':
                print("\n=== 文件分类规则 ===")
                for category, extensions in organizer.file_categories.items():
                    if extensions:
                        print(f"{category}: {', '.join(extensions)}")
                    else:
                        print(f"{category}: 其他未分类文件")
            
            else:
                print("无效命令，请重新输入")
                
        except Exception as e:
            print(f"错误：{e}")

if __name__ == "__main__":
    main()