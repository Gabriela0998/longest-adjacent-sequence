import sys


def main():
    file_names_list = pick_up_files()

    for file_name in file_names_list:
        print()
        try:
            matrix = read_file(f"test_files/{file_name}")
        except FileNotFoundError as err:
            print(f"Файл с име '{file_name}' не може да бъде намерен!")
        else:
            longest_sequence = find_longest_sequence(matrix)
            print(f"Най-дългата последователност за файла с име '{file_name}' е {longest_sequence}.")


def pick_up_files():
    print()
    print("Изберете от следните файлове: test1, test2, test3, test4. В случай, че желатете да въедете няколко файла, "
          "разделете имената им чрез запетаи)")

    file_names = input()

    return list(filter(lambda x: x != "", file_names.split(" ")))


def read_file(file):
    _file = open(file, "r")
    lines = _file.read().rstrip().split("\n")

    matrix = [[0] * int(lines[0].split(" ")[0]) for k in range(int(lines[0].split(" ")[1]))]
    lines.pop(0)

    for i, line in enumerate(lines):
        matrix[i] = line.split(" ")

    _file.close()

    return matrix


def find_sequence(matrix, i, j, buffer):
    if not is_valid(matrix, i, j):
        return None

    buffer[i][j] = matrix[i][j]
    sequence = 0

    if i > 0 and matrix[i - 1][j] == matrix[i][j] and buffer[i - 1][j] == 0:
        sequence = find_sequence(matrix, i - 1, j, list(map(list, buffer)))

    if j + 1 < len(matrix) and matrix[i][j + 1] == matrix[i][j] and buffer[i][j + 1] == 0:
        sequence = find_sequence(matrix, i, j + 1, list(map(list, buffer)))

    if i + 1 < len(matrix) and matrix[i + 1][j] == matrix[i][j] and buffer[i + 1][j] == 0:
        sequence = find_sequence(matrix, i + 1, j, list(map(list, buffer)))

    if j > 0 and matrix[i][j - 1] == matrix[i][j] and buffer[i][j - 1] == 0:
        sequence = find_sequence(matrix, i, j - 1, list(map(list, buffer)))

    return sequence + 1 if sequence else 1


def is_valid(matrix, i, j):
    return 0 <= i < len(matrix) and 0 <= j < len(matrix)


def find_longest_sequence(matrix):
    result = None
    res_size = -sys.maxsize

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):

            buffer = [[0] * len(matrix) for k in range(len(matrix))]

            sequence_count = find_sequence(matrix, i, j, buffer)

            if sequence_count > res_size:
                result = sequence_count
                res_size = sequence_count

    return result


if __name__ == '__main__':
    main()
