from sys import argv
import numpy as np


def find_median(data):
    if len(data)%2 == 1:
        return data[len(data)//2]
    else:
        return (data[len(data)//2] + data[len(data)//2 - 1])/2


def find_max(data):
    return data[-1]


def find_min(data):
    return data[0]


def find_middle(data):
    return sum(data)/len(data)


def main():
    file_name = argv[1]

    with open (file_name) as data_file:
        data_list = data_file.read().splitlines()

    for i, elem in enumerate(data_list):
        data_list[i] = int(elem)

    data_list = sorted(data_list)

    print("%.2f" % np.percentile(data_list, 90))
    print("%.2f" % find_median(data_list))
    print("%.2f" % find_max(data_list))
    print("%.2f" % find_min(data_list))
    print("%.2f" % find_middle(data_list))


if __name__ == "__main__":
    main()
