import random


def make_consistent_list(list_range):
    empty_list = []
    for x in range(list_range):
        empty_list.append(x)
    return empty_list


# Делает список с послдедовательными елементами

def make_random_list(list_range):
    empty_list = []
    for x in range(list_range):
        empty_list.append(random.randrange(0, list_range))
    return empty_list


# Делает список с радномными елементами

consistent_list_100 = make_consistent_list(100)
consistent_list_1k = make_consistent_list(1_000)
consistent_list_10k = make_consistent_list(10_000)
random_list_100 = make_random_list(100)
random_list_1k = make_random_list(1_000)
random_list_10k = make_random_list(10_000)

# задаем наши списки

print(random_list_100)
