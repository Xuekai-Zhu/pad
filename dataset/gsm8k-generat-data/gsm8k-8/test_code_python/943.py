def solution():
    # Calculate the profit per dozen donuts
    profit_per_dozen = 12 - (2.4 * 10)

    # Calculate the number of dozens needed to reach the goal
    dozens_needed = 96 / profit_per_dozen

    # Round up to the nearest whole number
    dozens_needed = math.ceil(dozens_needed)

    result = dozens_needed
    return result

print(solution())