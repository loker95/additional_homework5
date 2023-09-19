import random

matrix = []
sum_of_main_diagonal = 0
secondary_diagonal = []
user_number_of_row = int(input("выберите номер ряда "))
user_number_of_column = int(input("выберите номер столбика "))
column = []

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