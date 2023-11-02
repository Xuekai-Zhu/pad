def solution():
    # Calculate the number of chips remaining after Marnie's first 10
    remaining_chips = 100 - 10

    # Calculate the number of days it takes to eat the remaining chips
    days_to_finish = remaining_chips / 10

    # Add the first day to the total number of days
    total_days = days_to_finish + 1
    result = total_days
    return result

print(solution())