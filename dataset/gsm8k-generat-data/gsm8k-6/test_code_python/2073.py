def solution():
    # Calculate the weight of each pile
    remaining_jelly_beans = 36 - 6  # 6 ounces were eaten
    weight_each_pile = remaining_jelly_beans / 3  # remaining jelly beans are divided into 3 piles

    result = weight_each_pile
    return result

print(solution())