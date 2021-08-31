import numpy as np

n = int(input('Enter size: '))
mat = np.full((n, n), '_')
print(mat)


def check_matrix(matrix):
    n = matrix.shape[0]
    for i in range(n):
        if len(set(matrix[i])) == 1:
            if 'X' in matrix[i]:
                return 1
            elif 'O' in matrix[i]:
                return 2
    for i in range(n):
        if len(set(matrix[:, i])) == 1:
            if 'X' in matrix[:, i]:
                return 1
            elif 'O' in matrix[:, i]:
                return 2
    if len(set(matrix.diagonal())) == 1:
        if 'X' in matrix.diagonal():
            return 1
        elif 'O' in matrix.diagonal():
            return 2
    if len(set(np.fliplr(matrix).diagonal())) == 1:
        if 'X' in np.fliplr(matrix).diagonal():
            return 1
        elif 'O' in np.fliplr(matrix).diagonal():
            return 2
    if '_' not in matrix:
        return 0


while '_' in mat:
    # Player 1
    i, j = input('Player 1 enter location: ').split()
    i, j = int(i), int(j)
    while mat[i, j] != '_':
        i, j = input('Already taken, choose another location: ').split()
        i, j = int(i), int(j)
    if mat[i, j] == '_':
        mat[i, j] = 'X'
    print(mat)
    if check_matrix(mat) == 1:
        print('Player 1 wins')
        break
    if check_matrix(mat) == 0:
        print('Game tied')
        break

    # Player 2
    i, j = input('Player 2 enter location: ').split()
    i, j = int(i), int(j)
    while mat[i, j] != '_':
        i, j = input('Already taken, choose another location: ').split()
        i, j = int(i), int(j)
    if mat[i, j] == '_':
        mat[i, j] = 'O'
    print(mat)
    if check_matrix(mat) == 2:
        print('Player 2 wins')
        break
    if check_matrix(mat) == 0:
        print('Game tied')
        break
#end
