import numpy as np

n = int(input('Enter size: '))
mat = np.full((n, n), '_')
print(mat)


def player_input(number):
    i, j = input(f'Player {number} enter location: ').split()
    i, j = int(i), int(j)
    while mat[i, j] != '_':
        i, j = input('Already taken, choose another location: ').split()
        i, j = int(i), int(j)
    if mat[i, j] == '_':
        if number == 1:
            mat[i, j] = 'X'
        elif number == 2:
            mat[i, j] = 'O'
    print(mat)


def check_matrix(matrix):
    k = matrix.shape[0]
    for i in range(k):
        if len(set(matrix[i])) == 1:
            if 'X' in matrix[i]:
                return 1
            elif 'O' in matrix[i]:
                return 2
    for i in range(k):
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
    player_input(1)
    if check_matrix(mat) == 1:
        print('Player 1 wins')
        break
    if check_matrix(mat) == 0:
        print('Game tied')
        break

    # Player 2
    player_input(2)
    if check_matrix(mat) == 2:
        print('Player 2 wins')
        break
    if check_matrix(mat) == 0:
        print('Game tied')
        break


