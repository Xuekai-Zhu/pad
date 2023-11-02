def solution():
    """Rachel earned $200 babysitting. She spent 1/4 of the money on lunch. She spent 1/2 of the money on a DVD. How much did Rachel have left?"""
    # Calculate the amount spent on lunch
    lunch_cost = 200 * (1/4)

    # Calculate the amount spent on the DVD
    dvd_cost = 200 * (1/2)

    # Calculate the amount Rachel has left
    remaining_money = 200 - lunch_cost - dvd_cost

    # Display the remaining amount Rachel has
    result = remaining_money
    return result

print(solution())