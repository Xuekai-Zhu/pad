def solution():
    initial_sugar = 24
    reduction_factor = 0.5
    week = 4

    # Calculate the amount of sugar used for the cake on the fourth week
    sugar_used = initial_sugar * (reduction_factor ** (week - 1))

    result = sugar_used
    return result

print(solution())