def solution():
    total_meat = 20
    meatballs = 1/4 * total_meat
    spring_rolls = 3

    # Calculate the remaining meat after making meatballs and spring rolls
    remaining_meat = total_meat - meatballs - spring_rolls
    result = remaining_meat
    return result

print(solution())