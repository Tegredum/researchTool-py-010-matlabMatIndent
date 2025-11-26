# encoding: utf-8
# author: claude-sonnet-4-5-20250929-thinking-32k, Lingma
# python version: 3.10.16

import re

# 全局变量用于控制多行矩阵的缩进空格数
MATRIX_INDENT_SPACES = 4

def format_matlab_matrix(code_string, indent_spaces=None):
	"""
	格式化MATLAB代码中的矩阵，使各列元素对齐
	
	参数:
		code_string: 包含MATLAB矩阵的字符串
		indent_spaces: 多行矩阵的缩进空格数，默认为None，使用全局设置
	
	返回:
		格式化后的字符串
	"""
	
	# 如果提供了indent_spaces参数，则使用它，否则使用全局变量
	actual_indent_spaces = indent_spaces if indent_spaces is not None else MATRIX_INDENT_SPACES
	
	def find_matching_bracket(s, start):
		"""找到与start位置的'['匹配的']'位置"""
		count = 1
		i = start + 1
		while i < len(s) and count > 0:
			if s[i] == '[':
				count += 1
			elif s[i] == ']':
				count -= 1
			i += 1
		return i - 1 if count == 0 else -1
	
	def parse_and_format_matrix(matrix_str):
		"""解析并格式化单个矩阵"""
		# 提取括号内的内容
		content = matrix_str[1:-1].strip()
		
		if not content:
			return '[]'
		
		# 检查是否包含嵌套的括号（如元胞数组），暂不处理
		if '[' in content or ']' in content:
			return matrix_str
		
		# 分割行（支持分号和换行符）
		rows = re.split(r'[;\n]', content)
		
		matrix = []
		for row in rows:
			row = row.strip()
			if row:
				# 分割列元素（支持逗号、空格、制表符）
				elements = re.split(r'[,\s]+', row)
				elements = [e.strip() for e in elements if e.strip()]
				if elements:
					matrix.append(elements)
		
		if not matrix:
			return '[]'
		
		# 计算每列的最大宽度
		num_cols = max(len(row) for row in matrix)
		col_widths = [0] * num_cols
		
		for row in matrix:
			for i, elem in enumerate(row):
				col_widths[i] = max(col_widths[i], len(elem))
		
		# 格式化每一行，右对齐数字
		formatted_rows = []
		for row in matrix:
			formatted_elements = []
			for i in range(len(row)):
				formatted_elements.append(row[i].rjust(col_widths[i]))
			formatted_rows.append('  '.join(formatted_elements))
		
		# 组合成最终的矩阵字符串
		if len(formatted_rows) == 1:
			# 单行矩阵
			return '[' + formatted_rows[0] + ']'
		else:
			# 多行矩阵
			result = '[\n'
			indent = ' ' * actual_indent_spaces
			for row in formatted_rows:
				result += indent + row + '\n'
			result += ']'
			return result
	
	# 查找并处理所有矩阵
	result = []
	i = 0
	
	while i < len(code_string):
		if code_string[i] == '[':
			# 找到匹配的右括号
			end = find_matching_bracket(code_string, i)
			if end != -1:
				matrix_str = code_string[i:end+1]
				formatted = parse_and_format_matrix(matrix_str)
				result.append(formatted)
				i = end + 1
			else:
				result.append(code_string[i])
				i += 1
		else:
			result.append(code_string[i])
			i += 1
	
	return ''.join(result)


