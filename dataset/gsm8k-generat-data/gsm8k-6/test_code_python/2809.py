def solution():
    # Calculate the increase in the value of Jenny's house
    increase = 0.25 * 400000

    # Calculate the new value of Jenny's house after the high-speed rail project
    new_value = 400000 + increase

    # Calculate the maximum value of improvements Jenny can make to her house
    max_improvements = ((0.02 * new_value) - 15000) / 0.02
    result = max_improvements
    return result

print(solution())