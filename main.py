import random

matrix = []
sum_of_main_diagonal = 0
secondary_diagonal = []
user_number_of_row = int(input("выберите номер ряда "))
user_number_of_column = int(input("выберите номер столбика "))
column = []
number_of_row_to_change = int(input("выберите номер рядка для замены "))
number_of_row_to_change_on = int(input("на какой номер радка поменять "))
number_of_col_to_swap = int(input("выберите номер столбца для замены "))
number_of_col_to_swap_on = int(input("на какой столбец поменять "))

for i in range(10):
    row = [random.randint(1, 100) for j in range(10)]
    matrix.append(row)

for row in matrix:
    print(row)

for i in range(10):
    for j in range(10):
        if i == j:
            sum_of_main_diagonal += matrix[i][j]
        if i + j == 9:
            secondary_diagonal.append(matrix[i][j])

for row in matrix:
    column.append(row[user_number_of_column])


print(sum_of_main_diagonal, 'sum of main diagonal')
print(max(secondary_diagonal), min(secondary_diagonal), "max, min")
print("digits in a row ", user_number_of_row, matrix[user_number_of_row])
print("digits in a column ", user_number_of_column, column)

matrix[number_of_row_to_change], matrix[number_of_row_to_change_on] = matrix[number_of_row_to_change_on], matrix[number_of_row_to_change]
print("с заменой рядока")
for row in matrix:
    print(row)

print("с заменой столбца")
for row in matrix:
    matrix[number_of_col_to_swap], matrix[number_of_col_to_swap_on] = matrix[number_of_col_to_swap_on], matrix[number_of_col_to_swap]
    print(row)