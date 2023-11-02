def solution():
    # Calculate the total number of toothbrushes given away
    total_given_away = 53 + 67 + 46 + (330 - 53 - 67 - 46) / 2 + (330 - 53 - 67 - 46) / 2 

    # Determine the number of toothbrushes given away in the busiest and slowest months
    busiest_month = (330 - total_given_away) / 2  # half of the remaining toothbrushes distributed in April
    slowest_month = 46
    difference = busiest_month - slowest_month
    result = difference
    return result

print(solution())