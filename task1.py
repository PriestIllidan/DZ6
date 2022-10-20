# Задача 1. Создайте программу для игры в "Крестики-нолики".
matrix = list(range(1, 10))


def print_matrix(matrix):
    print(matrix[:3])
    print(matrix[3:6])
    print(matrix[6:])


def check_win(matrix):
    if matrix[0] == matrix[3] == matrix[6] or matrix[1] == matrix[4] == matrix[7] or matrix[2] == matrix[5] == matrix[8]:
        return True
    elif matrix[0] == matrix[1] == matrix[2] or matrix[3] == matrix[4] == matrix[5] or matrix[6] == matrix[7] == matrix[8]:
        return True
    elif matrix[0] == matrix[4] == matrix[8] or matrix[2] == matrix[4] == matrix[6]:
        return True


def x_o(matrix):
    count = 0
    while count < 9:
        first_player = int(input("Укажите координату х: "))
        matrix[first_player-1] = "x"
        if check_win(matrix) == True:
            print("Вы выиграли")
            print_matrix(matrix)
            return matrix
        count += 1
        if count == 9:
            print("Ничья")
            return matrix
        second_player = int(input("Укажите координату o: "))
        matrix[second_player-1] = "o"
        if check_win(matrix) == True:
            print("Вы выиграли")
            print_matrix(matrix)
            return matrix
        print_matrix(matrix)
        count += 1
        print(count)
    print("Ничья")
    return matrix


matrix1 = x_o(matrix)
print_matrix(matrix1)