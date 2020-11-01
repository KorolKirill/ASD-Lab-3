import time


def bubbleSort(given_list):
    start = time.time()

    list_len = len(given_list)
    for x in range(list_len):
        for y in range(list_len - 1):
            if given_list[y] > given_list[y + 1]:
                save_element = given_list[y]
                given_list[y] = given_list[y + 1]
                given_list[y + 1] = save_element

    end = time.time()
    estimatedTime = "BubbleSort sort for " + str(list_len) + " elements took " + str(end - start) + " seconds"

    return estimatedTime
