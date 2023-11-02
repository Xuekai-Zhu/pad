def solution():
    """There are 21 cherry tomatoes on the tomato plant. 2 birds eat one-third of the tomatoes. How many are still left on the tomato plant?"""
    total_tomatoes = 21
    eaten_tomatoes = (1/3) * total_tomatoes * 2
    remaining_tomatoes = total_tomatoes - eaten_tomatoes
    result = remaining_tomatoes
    return result

print(solution())