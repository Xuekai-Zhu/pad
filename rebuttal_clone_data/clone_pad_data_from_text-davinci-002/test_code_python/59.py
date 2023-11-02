def solution():
    """Every hour Joanne has to collect the coins out of the fountain inside the mall. During the first hour, she collected 15 coins. For the next two hours, she collected 35 coins from the fountain. In the fourth hour, she collected 50 coins from the fountain but she gave 15 of them to her coworker so she could buy a soda. How many coins did she have after the fourth hour?"""
    hour_one = 15
    hour_two = 35
    hour_three = 35
    hour_four = 50
    coins_given_away = 15
    total_coins = hour_one + hour_two + hour_three + hour_four - coins_given_away
    result = total_coins
    return result

print(solution())