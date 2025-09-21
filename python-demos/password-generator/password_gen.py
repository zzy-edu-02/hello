#!/usr/bin/env python3
"""
密码生成器
生成安全的随机密码
"""

import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, 
                     use_digits=True, use_symbols=True):
    """生成随机密码"""
    characters = ""
    
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    if not characters:
        return "错误：至少需要选择一种字符类型"
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def check_password_strength(password):
    """检查密码强度"""
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("密码长度应至少8位")
    
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("建议包含小写字母")
    
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("建议包含大写字母")
    
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("建议包含数字")
    
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
        score += 1
    else:
        feedback.append("建议包含特殊字符")
    
    strength_levels = ["很弱", "弱", "一般", "强", "很强"]
    strength = strength_levels[min(score, 4)]
    
    return strength, feedback

def main():
    """主函数"""
    print("=== 密码生成器 ===")
    print("功能:")
    print("1. generate - 生成新密码")
    print("2. check <密码> - 检查密码强度")
    print("3. quit - 退出程序")
    
    while True:
        try:
            command = input("\n请输入命令: ").strip().split(' ', 1)
            action = command[0].lower()
            
            if action == 'quit':
                print("再见！")
                break
            
            elif action == 'generate':
                print("\n=== 密码生成设置 ===")
                length = int(input("密码长度 (默认12): ") or "12")
                
                use_uppercase = input("包含大写字母? (y/n, 默认y): ").lower() != 'n'
                use_lowercase = input("包含小写字母? (y/n, 默认y): ").lower() != 'n'
                use_digits = input("包含数字? (y/n, 默认y): ").lower() != 'n'
                use_symbols = input("包含特殊字符? (y/n, 默认y): ").lower() != 'n'
                
                password = generate_password(
                    length, use_uppercase, use_lowercase, use_digits, use_symbols
                )
                
                print(f"\n生成的密码: {password}")
                
                # 检查生成密码的强度
                strength, feedback = check_password_strength(password)
                print(f"密码强度: {strength}")
                if feedback:
                    print("建议: " + ", ".join(feedback))
            
            elif action == 'check' and len(command) > 1:
                password = command[1]
                strength, feedback = check_password_strength(password)
                print(f"密码强度: {strength}")
                if feedback:
                    print("改进建议: " + ", ".join(feedback))
                else:
                    print("这是一个强密码！")
            
            else:
                print("无效命令，请重新输入")
                
        except ValueError:
            print("错误：请输入有效的数字")
        except Exception as e:
            print(f"错误：{e}")

if __name__ == "__main__":
    main()