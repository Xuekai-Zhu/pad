def solution():
    # Calculate the number of buyers on the first day
    day1_buyers = 50

    # Calculate the number of buyers on the second day
    day2_buyers = day1_buyers / 2 + 40

    # Calculate the total number of buyers
    total_buyers = day1_buyers + day2_buyers + 40

    result = total_buyers
    return result

print(solution())