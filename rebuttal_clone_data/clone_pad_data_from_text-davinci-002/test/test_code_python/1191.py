def solution():
    coins_first_hour = 20
    coins_second_hour = 30
    coins_third_hour = 30
    coins_fourth_hour = 40
    coins_fifth_hour = 20
    total_coins = coins_first_hour + coins_second_hour + coins_third_hour + coins_fourth_hour - coins_fifth_hour
    result = total_coins
    return result

print(solution())