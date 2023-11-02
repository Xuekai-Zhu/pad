def solution():
    # Calculate the total number of coins collected in the first three hours
    total_coins_first_three_hours = 15 + 35 + 35

    # Calculate the total number of coins collected and given away in the fourth hour
    total_coins_fourth_hour = 50 - 15

    # Calculate the total number of coins Joanne has after the fourth hour
    total_coins = total_coins_first_three_hours + total_coins_fourth_hour
    result = total_coins
    return result

print(solution())