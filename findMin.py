import timeit
import numpy as np


def bin_find_min_array(array):
    if array is None or len(array) == 0:
        print('invalid or empty array!')
        exit(-1)
    else:
        return bin_find_min_array_not_empty(array)


def bin_find_min_array_not_empty(array):

    if len(array) == 1:
        return array[0]
    else:
        middle_index = len(array) // 2
        min_left = bin_find_min_array_not_empty(array[:middle_index])
        min_right = bin_find_min_array_not_empty(array[middle_index:])
        if min_left < min_right:
            return min_left
        else:
            return min_right


np_arr = np.random.randint(100, 1000, size=1000000)
starttime = timeit.default_timer()
print(bin_find_min_array(np_arr))
print("The time difference is :", timeit.default_timer() - starttime)




