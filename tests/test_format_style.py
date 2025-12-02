#!/usr/bin/env python3
# encoding: utf-8
# author: claude-sonnet-4-5-20250929-thinking-32k, Lingma
# python version: 3.12.8

import sys
import os

# Add the src directory to the path so we can import matFormatter
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from matFormatter import format_matlab_matrix

if __name__ == "__main__":
    # 示例1：测试默认格式样式（分号）
    matlab_code1 = """A = [1 2 3; 4 5 6; 7 8 9]"""
    print("示例1 (默认格式样式 - 分号):")
    print(format_matlab_matrix(matlab_code1))
    print()

    # 示例2：显式指定分号格式
    print("示例2 (显式指定分号格式):")
    print(format_matlab_matrix(matlab_code1, format_style='semicolon'))
    print()

    # 示例3：测试空格格式样式
    print("示例3 (空格格式样式):")
    print(format_matlab_matrix(matlab_code1, format_style='space'))
    print()

    # 示例4：测试带有缩进的空格格式样式
    print("示例4 (空格格式样式，自定义缩进为2):")
    print(format_matlab_matrix(matlab_code1, format_style='space', indent_spaces=2))
    print()

    # 示例5：测试带有缩进的空格格式样式
    print("示例5 (空格格式样式，自定义缩进为6):")
    print(format_matlab_matrix(matlab_code1, format_style='space', indent_spaces=6))
    print()

    # 示例6：测试复杂矩阵的分号格式
    matlab_code2 = """B = [10 200 3000 40000; 5 60 700 8000; 9 80 700 6000]"""
    print("示例6 (复杂矩阵，分号格式):")
    print(format_matlab_matrix(matlab_code2))
    print()

    # 示例7：测试复杂矩阵的空格格式
    print("示例7 (复杂矩阵，空格格式):")
    print(format_matlab_matrix(matlab_code2, format_style='space'))
    print()

    # 示例8：测试左对齐+空格格式
    print("示例8 (左对齐 + 空格格式):")
    print(format_matlab_matrix(matlab_code2, format_style='space', alignment='left'))
    print()

    # 示例9：测试右对齐+空格格式
    print("示例9 (右对齐 + 空格格式):")
    print(format_matlab_matrix(matlab_code2, format_style='space', alignment='right'))
    print()

    # 示例10：测试右对齐+分号格式
    print("示例10 (右对齐 + 分号格式):")
    print(format_matlab_matrix(matlab_code2, format_style='semicolon', alignment='right'))
    print()

    # 示例11：测试逗号分隔的输入
    matlab_code3 = """C = [1.5, 2.345, 3; 44.2, 5, 6.78]"""
    print("示例11 (逗号分隔输入，分号格式输出):")
    print(format_matlab_matrix(matlab_code3))
    print()

    # 示例12：测试逗号分隔输入的空格格式输出
    print("示例12 (逗号分隔输入，空格格式输出):")
    print(format_matlab_matrix(matlab_code3, format_style='space'))
    print()

    # 示例13：测试左对齐长元素矩阵
    matlab_code4 = """D = [1.23456 2.34 300000; 4 55555.5 6.7]"""
    print("示例13 (左对齐长元素矩阵，分号格式):")
    print(format_matlab_matrix(matlab_code4, format_style='semicolon', alignment='left'))
    print()

    # 示例14：测试右对齐长元素矩阵
    print("示例14 (右对齐长元素矩阵，分号格式):")
    print(format_matlab_matrix(matlab_code4, format_style='semicolon', alignment='right'))