def solution():
    # Calculate the total amount of money Bob has already won
    total_money = 100 * 2

    # Calculate the amount of money left for Bob to save up
    amount_left = 1000 - total_money

    # Calculate the minimum number of additional weeks Bob must win first place
    minimum_weeks = amount_left // 100
    if amount_left % 100 != 0:
        minimum_weeks += 1

    result = minimum_weeks
    return result

print(solution())