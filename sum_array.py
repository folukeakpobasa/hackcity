nums = [1, 2, 3, 4]
sum_new_nums = [sum(nums[:index]) for index in range(1, len(nums)+1)]
print(sum_new_nums)

