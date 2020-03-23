import random
import datetime

# 1
names_list = ['Аня', 'Артур', 'Ильнур', 'Наиль', 'Алексей', 'Лена', 'Ксюша', 'Костя', 'Маша', 'Таня', 'Рая', 'Ясна',
              'Север', 'Грег', 'Майя', 'Люба', 'Саша', 'Катя', 'Илья', 'Андрей']


def get_names(names, count):
    names_new = []
    for i in range(0, count):
        idx = random.randint(0, len(names) - 1)
        names_new.append(names[idx])
    return names_new


def get_count(names):
    names_count = dict.fromkeys(names, 0)
    for name in names:
        names_count[name] += 1
    return names_count


# 2
def get_name_most_often(names):
    names_count = get_count(names)
    names_count_most_often = sorted(
        list(names_count.values()),
        reverse=True
    )[0]
    name_most_often = [key for (key, value) in names_count.items() if value == names_count_most_often]

    return name_most_often[0], names_count_most_often


# 3
def get_rarely_letter(names):
    letters = [i[0] for i in names]
    letters_count = get_count(letters)
    letters_count_most_rarely = sorted(list(letters_count.values()))[0]
    letter_most_rarely = [key for (key, value) in letters_count.items() if value == letters_count_most_rarely]

    return letter_most_rarely[0], letters_count_most_rarely


# 4
def get_latest_log(logs):
    dates = []
    file = open(logs, 'rb').readlines()
    for line in file:
        dates.append(datetime.datetime.strptime(line.decode().split(' - ')[0], '%Y-%m-%d %H:%M:%S,%f'))

    return max([c for c in dates])

