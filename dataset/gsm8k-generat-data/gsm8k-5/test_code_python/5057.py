def solution():
    initial_tomatoes = 21  # There are 21 cherry tomatoes on the tomato plant
    eaten_tomatoes = 2 * (1/3) * initial_tomatoes  # 2 birds eat one-third of the tomatoes
    remaining_tomatoes = initial_tomatoes - eaten_tomatoes  # Calculate the remaining tomatoes
    result = remaining_tomatoes
    return result

print(solution())