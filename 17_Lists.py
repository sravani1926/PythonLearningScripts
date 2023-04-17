names=['Lee','Navya','Apple','Cherry','Duffer']
print(names)
print(names[2:])
print(names[-1])
print(names[2:4])

#2D Lists

matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix)
print(matrix[0][1])

for row in matrix:
    for item in row:
        print(item)