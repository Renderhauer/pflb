from sys import argv


def to_munix_time(time):
    return str(int(time[:time.find(':')])*60 + int(time[time.find(':')+1:]))


def from_munix_time(time):
    if (time%60) < 10:
        x = '0' + str(time%60)
    else:
        x = time%60
    return str(time//60) + ':' + str(x)


def main():
    file_name = argv[1]
    timestamps = {}

    with open (file_name) as data:
        data_list = data.read().splitlines()

    for i, data in enumerate(data_list):
        data_list[i] = to_munix_time(data[:data.find(' ')]) + ' ' + to_munix_time(data[data.find(' ')+1:])

    maximum = 0
    for time in range(480, 1201):
        counter = 0
        for user in data_list:
            income = int(user[:user.find(' ')])
            outcome = int(user[user.find(' ')+1:])
            if time >= income and time < outcome:
                counter += 1
        if counter > maximum:
            maximum = counter
        timestamps.update({time:counter})

    lasting = False
    for time in range(480, 1201):
        if timestamps.get(time) == maximum and lasting == False:
            print(from_munix_time(time), end=' ')
            lasting = True
        if timestamps.get(time) != maximum and lasting == True:
            print(from_munix_time(time))
            lasting = False


if __name__ == "__main__":
    main()
