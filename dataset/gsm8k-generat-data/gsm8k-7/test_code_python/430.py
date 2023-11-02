def solution():
    pears = 6
    apples = 4
    pineapples = 2
    total_fruit = pears + apples + pineapples + 1  # Add 1 for the basket of plums
    remaining_fruit = 9
    lost_fruit = total_fruit - remaining_fruit
    lost_plums = lost_fruit - 6 - 4 - 2  # Subtract the other types of fruit
    result = lost_plums
    return result

print(solution())