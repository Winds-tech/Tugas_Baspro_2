matrix1 = [
    [1, 2, 3, 4, 5],
    [2, 2, 4, 2, 4],
    [3, 5, 2, 5, 2],
    [4, 2, 1, 2, 1],
    [5, 3, 2, 3, 3]
]

matrix2 = [
    [5, 4, 3, 2, 1],
    [4, 2, 4, 2, 4],
    [3, 5, 2, 5, 2],
    [2, 2, 1, 2, 1],
    [1, 3, 2, 3, 3]
]

result_matrix = []
for i in range(len(matrix1)):
    row = []
    for j in range(len(matrix2[0])):
        sum = 0
        for k in range(len(matrix2)):
            sum += matrix1[i][k] * matrix2[k][j]
        row.append(sum)
    result_matrix.append(row)

# hasil
print("Hasil perkalian matriks:")
for row in result_matrix:
    print(row)