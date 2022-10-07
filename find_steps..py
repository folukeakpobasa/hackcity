
def num_of_steps(num):
    steps = 0
    if num == 0:
        return 0
    while num > 0:
        print (num)
        # steps = steps + 1
        if num % 2 == 0:
            num = num / 2
            steps = steps + 1
            print(num)
        else:
            floor_num = num // 2
            num = floor_num - 1
            steps = steps + 1
            print(num)

        # if num % 2 == 1:
        #     num = num // 2
        #     steps = steps + 1

        # else:
        #     num = num / 2
        #     steps = steps + 1

    return steps


print(num_of_steps(14))
