def print_spiral(matrix):
	if len(matrix) == 0:
		return

	# Initialize pointers to traverse matrix
	row_start = 0
	row_end = len(matrix[0])
	col_start = 0
	col_end = len(matrix)

	while row_start < row_end and col_start < col_end:
		
		# Move right
		for num in range(row_start, row_end):
			print str(matrix[col_start][num]),
		
		# Move down
		for num in range(col_start + 1, col_end):
			print str(matrix[num][row_end - 1]),

		# Move left
		if (col_end - col_start > 1):
			for num in reversed(range(row_start, row_end - 1)):
				print str(matrix[col_end - 1][num]),
		
		# Move up
		if (row_end - row_start > 1):
			for num in reversed(range(col_start + 1, col_end - 1)):
				print str(matrix[num][row_start]),

		# Update pointers
		col_start += 1
		row_end -= 1
		col_end -= 1
		row_start += 1


matrix = \
[[11, 12, 13, 14, 15],
[21, 22, 23, 24, 25],
[31, 32, 33, 34, 35],
[41, 42, 43, 44, 45]]

print_spiral(matrix)
