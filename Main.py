import random
import time

start = time.time()


# Зассекает время

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

def bubble_sort(given_list):
    list_len = len(given_list)
    for x in range(list_len):
        for y in range(list_len - 1):
            if given_list[y] > given_list[y + 1]:
                save_element = given_list[y]
                given_list[y] = given_list[y + 1]
                given_list[y + 1] = save_element
    return given_list


print(random_list_100)

end = time.time()
print(end - start)

# Пишет сколько было затраченно времени в секундах, !Должно быть в самом конце
