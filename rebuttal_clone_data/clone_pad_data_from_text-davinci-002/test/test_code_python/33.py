def solution():
    
    hour_one = 15
    hour_two = 35
    hour_three = 35
    hour_four = 50
    coins_given_away = 15
    total_coins = hour_one + hour_two + hour_three + hour_four - coins_given_away
    result = total_coins
    return result

print(solution())