#!/usr/bin/env python3
"""
简单的待办事项管理器
支持添加、删除、查看待办事项
"""

import json
import os
from datetime import datetime

class TodoList:
    def __init__(self, filename="todos.json"):
        self.filename = filename
        self.todos = self.load_todos()
    
    def load_todos(self):
        """从文件加载待办事项"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def save_todos(self):
        """保存待办事项到文件"""
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.todos, f, ensure_ascii=False, indent=2)
    
    def add_todo(self, task):
        """添加新的待办事项"""
        todo = {
            'id': len(self.todos) + 1,
            'task': task,
            'completed': False,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.todos.append(todo)
        self.save_todos()
        print(f"已添加待办事项: {task}")
    
    def remove_todo(self, todo_id):
        """删除待办事项"""
        for i, todo in enumerate(self.todos):
            if todo['id'] == todo_id:
                removed_task = self.todos.pop(i)
                self.save_todos()
                print(f"已删除待办事项: {removed_task['task']}")
                return
        print(f"未找到ID为 {todo_id} 的待办事项")
    
    def complete_todo(self, todo_id):
        """标记待办事项为完成"""
        for todo in self.todos:
            if todo['id'] == todo_id:
                todo['completed'] = True
                self.save_todos()
                print(f"已完成待办事项: {todo['task']}")
                return
        print(f"未找到ID为 {todo_id} 的待办事项")
    
    def list_todos(self):
        """显示所有待办事项"""
        if not self.todos:
            print("暂无待办事项")
            return
        
        print("\n=== 待办事项列表 ===")
        for todo in self.todos:
            status = "✓" if todo['completed'] else "○"
            print(f"{status} [{todo['id']}] {todo['task']} ({todo['created_at']})")

def main():
    """主函数"""
    todo_list = TodoList()
    
    print("=== 待办事项管理器 ===")
    print("命令:")
    print("1. add <任务内容> - 添加新任务")
    print("2. remove <任务ID> - 删除任务")
    print("3. complete <任务ID> - 完成任务")
    print("4. list - 显示所有任务")
    print("5. quit - 退出程序")
    
    while True:
        try:
            command = input("\n请输入命令: ").strip().split(' ', 1)
            action = command[0].lower()
            
            if action == 'quit':
                print("再见！")
                break
            elif action == 'add' and len(command) > 1:
                todo_list.add_todo(command[1])
            elif action == 'remove' and len(command) > 1:
                todo_list.remove_todo(int(command[1]))
            elif action == 'complete' and len(command) > 1:
                todo_list.complete_todo(int(command[1]))
            elif action == 'list':
                todo_list.list_todos()
            else:
                print("无效命令，请重新输入")
                
        except ValueError:
            print("错误：请输入有效的任务ID")
        except Exception as e:
            print(f"错误：{e}")

if __name__ == "__main__":
    main()