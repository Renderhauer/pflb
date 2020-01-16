from sys import argv, platform


def main():
    file_path = argv[1]

    if platform == "linux" or platform == "linux2":
        if file_path[-1:] != r'/':
            file_path = file_path + r'/'
    else:
        if file_path[-1:] != r'\n\n\\'[:-1]:
            file_path += r'\n\n\\'[:-1]

    with open (file_path + 'Cash1.txt') as data:
        data_1 = data.read().splitlines()
    with open (file_path + 'Cash2.txt') as data:
        data_2 = data.read().splitlines()
    with open (file_path + 'Cash3.txt') as data:
        data_3 = data.read().splitlines()
    with open (file_path + 'Cash4.txt') as data:
        data_4 = data.read().splitlines()
    with open (file_path + 'Cash5.txt') as data:
        data_5 = data.read().splitlines()

    maximum = 0
    total = []
    for i in range(0, 16):
        total.append(float(data_1[i]) + float(data_2[i]) + float(data_3[i]) + float(data_4[i]) + float(data_5[i]))
        if total[i] > maximum:
            maximum = total[i]

    for i in range(0, 16):
        if total[i] == maximum:
            print(i+1)
            break


if __name__ == "__main__":
    main()
