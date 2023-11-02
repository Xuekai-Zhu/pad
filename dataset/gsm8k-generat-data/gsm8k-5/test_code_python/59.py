def solution():
    # Coins collected in the first hour
    coins_first_hour = 15

    # Coins collected in the next two hours
    coins_next_two_hours = 35 * 2

    # Coins collected in the fourth hour, minus 15 given away
    coins_fourth_hour = 50 - 15

    # Total coins collected after four hours
    total_coins = coins_first_hour + coins_next_two_hours + coins_fourth_hour
    result = total_coins
    return result

print(solution())