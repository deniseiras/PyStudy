# best
def centered_average(nums):
    small = min(nums)
    big = max(nums)
    return (sum(nums) - small - big) / (len(nums) - 2)


# def centered_average(nums):
#     # array = [1,1, 2, 10, 2, 10]
#     # array = [1,1, 1]
#     array = nums
#
#     max = array[0]
#     min = array[0]
#
#     for each in array:
#         if each > max:
#             max = each
#         if each < min:
#             min = each
#
#     # # assume first
#     idx_max = array.index(max)
#     print(idx_max)
#     idx_min = array.index(min)
#     print(idx_min)
#
#
#     # BUG !!! last element no removed when is max
#     array[idx_max:-1] = array[idx_max + 1:-1]
#     print(array)
#     array[idx_min:-1] = array[idx_min + 1:-1]
#     print(array)
#
#     summ = 0
#     for each in array:
#         summ += each
#
#     centered_avg = int(summ / len(array))
#     return centered_avg

# BUG !!! last element no removed
print(centered_average([1, 2, 3, 4, 100]))

