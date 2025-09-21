#!/usr/bin/env python3
"""
简单的命令行计算器
支持基本的四则运算
"""

def add(x, y):
    """加法"""
    return x + y

def subtract(x, y):
    """减法"""
    return x - y

def multiply(x, y):
    """乘法"""
    return x * y

def divide(x, y):
    """除法"""
    if y == 0:
        return "错误：除数不能为零"
    return x / y

def main():
    """主函数"""
    print("=== 简单计算器 ===")
    print("支持的操作:")
    print("1. 加法 (+)")
    print("2. 减法 (-)")
    print("3. 乘法 (*)")
    print("4. 除法 (/)")
    print("输入 'quit' 退出程序")
    
    while True:
        try:
            # 获取用户输入
            expression = input("\n请输入计算表达式 (例如: 5 + 3): ").strip()
            
            if expression.lower() == 'quit':
                print("再见！")
                break
            
            # 解析表达式
            parts = expression.split()
            if len(parts) != 3:
                print("错误：请输入正确的格式 (数字 操作符 数字)")
                continue
            
            num1 = float(parts[0])
            operator = parts[1]
            num2 = float(parts[2])
            
            # 执行计算
            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            else:
                print("错误：不支持的操作符")
                continue
            
            print(f"结果: {num1} {operator} {num2} = {result}")
            
        except ValueError:
            print("错误：请输入有效的数字")
        except Exception as e:
            print(f"错误：{e}")

if __name__ == "__main__":
    main()