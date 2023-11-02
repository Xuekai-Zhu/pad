def solution():
    total_acorns = 210

    # Divide the total acorns into 3 equal parts for each winter month
    acorns_per_month = total_acorns / 3

    # Subtract 60 acorns from each month's pile that the squirrel left for winter
    acorns_left = acorns_per_month - 60

    # Add up the acorns that the squirrel took from each month's pile
    acorns_taken = acorns_left * 3

    result = acorns_taken
    return result

print(solution())