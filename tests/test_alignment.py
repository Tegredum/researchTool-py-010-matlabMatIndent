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
    # 示例1：测试默认左对齐
    matlab_code1 = """A = [1.5 22.345 333; 4444 5 6.78]"""
    print("示例1 (默认左对齐):")
    print(format_matlab_matrix(matlab_code1))
    print()

    # 示例2：测试明确指定左对齐
    print("示例2 (明确指定左对齐):")
    print(format_matlab_matrix(matlab_code1, alignment='left'))
    print()

    # 示例3：测试右对齐
    print("示例3 (右对齐):")
    print(format_matlab_matrix(matlab_code1, alignment='right'))
    print()

    # 示例4：测试多行矩阵左对齐
    matlab_code2 = """B = [
    1 222 3333
    44444 5 66
    77 8888 9
    ]"""
    print("示例4 (多行矩阵，默认左对齐):")
    print(format_matlab_matrix(matlab_code2))
    print()

    # 示例5：测试多行矩阵右对齐
    print("示例5 (多行矩阵，右对齐):")
    print(format_matlab_matrix(matlab_code2, alignment='right'))
    print()

    # 示例6：测试混合对齐效果
    matlab_code3 = """C = [1 2222 3; 44 55 66666]"""
    print("示例6 (混合长度元素，默认左对齐):")
    print(format_matlab_matrix(matlab_code3))
    print()

    print("示例7 (混合长度元素，右对齐):")
    print(format_matlab_matrix(matlab_code3, alignment='right'))
    print()

    # 示例8：测试带自定义缩进和对齐方式
    print("示例8 (自定义缩进2个空格 + 右对齐):")
    print(format_matlab_matrix(matlab_code1, indent_spaces=2, alignment='right'))
    print()

    print("示例9 (自定义缩进6个空格 + 左对齐):")
    print(format_matlab_matrix(matlab_code1, indent_spaces=6, alignment='left'))
