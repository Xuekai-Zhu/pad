def solution():
    # Calculate the total number of tins collected in the first three days
    total_tins = 50 + 3*50 + (3*50 - 50)

    # Calculate the number of tins still needed to reach 500
    remaining_tins = 500 - total_tins

    # Calculate the average number of tins to collect per day for the remaining days
    average_tins = remaining_tins / 4

    result = average_tins
    return result

print(solution())