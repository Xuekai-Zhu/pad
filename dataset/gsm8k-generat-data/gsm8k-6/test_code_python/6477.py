def solution():
    # Find the total amount Jackson needs to raise on the remaining 3 days
    remaining_amount = 1000 - 300 - 40

    # Calculate the remaining houses Jackson needs to visit to meet his goal
    houses_per_day = (remaining_amount / 3) * 4 // 10  # use integer division to round down to the nearest whole number of houses
    result = houses_per_day
    return result

print(solution())