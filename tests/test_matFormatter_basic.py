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
	# 示例1：多行多列矩阵
	matlab_code1 = """A = [1 2 3; 4 5 6; 7 8 9]"""
	print("示例1:")
	print(format_matlab_matrix(matlab_code1))
	print()
	
	# 示例2：已经是多行格式但未对齐
	matlab_code2 = """B = [
	1 22 333
	4444 55 6
	7 888 9
	]"""
	print("示例2:")
	print(format_matlab_matrix(matlab_code2))
	print()
	
	# 示例3：包含小数
	matlab_code3 = """C = [1.5, 2.345, 3; 44.2, 5, 6.78]"""
	print("示例3:")
	print(format_matlab_matrix(matlab_code3))
	print()
	
	# 示例4：多个矩阵
	matlab_code4 = """X = [1 2; 3 4]; Y = [10 20 30; 40 50 60]"""
	print("示例4:")
	print(format_matlab_matrix(matlab_code4))
	print()
	
	# 示例5：测试默认4空格缩进
	matlab_code5 = """D = [1 22 333; 4444 5 66; 7 88 999]"""
	print("示例5 (默认4空格缩进):")
	print(format_matlab_matrix(matlab_code5))
	print()
	
	# 示例6：测试自定义缩进（2个空格）
	print("示例6 (自定义2空格缩进):")
	print(format_matlab_matrix(matlab_code5, indent_spaces=2))
	print()
	
	# 示例7：测试自定义缩进（6个空格）
	print("示例7 (自定义6空格缩进):")
	print(format_matlab_matrix(matlab_code5, indent_spaces=6))
