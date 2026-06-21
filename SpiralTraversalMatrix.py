#Write a program to print the spiral traversal of a given matrix.
rows, cols =map(int, input().split())
matrix = []
for _ in range(rows):
    matrix.append(list(map(int, input().split())))
print("Spiral Traversal of the matrix is:", end=" ")
top, bottom = 0, rows - 1
left, right = 0, cols - 1
result = []
while top <= bottom and left <= right:
    for i in range(left, right + 1):
        result.append(matrix[top][i])
    top += 1
    for i in range(top, bottom +1):
        result.append(matrix[i][right])
    right -= 1
    if top <= bottom:
        for i in range(right, left-1, -1):
            result.append(matrix[bottom][i])
        bottom -= 1
    if left <= right:
        for i in range(bottom, top - 1, -1):
            result.append(matrix[i][left])
        left += 1
print(' '.join(map(str, result)))
