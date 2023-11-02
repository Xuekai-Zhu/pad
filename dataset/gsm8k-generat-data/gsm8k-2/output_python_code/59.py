def solution():
    """Every hour Joanne has to collect the coins out of the fountain inside the mall. During the first hour, she collected 15 coins. For the next two hours, she collected 35 coins from the fountain. In the fourth hour, she collected 50 coins from the fountain but she gave 15 of them to her coworker so she could buy a soda. How many coins did she have after the fourth hour?"""
    total_coins = 0
    total_coins += 15 # hour 1
    total_coins += 35 # hour 2
    total_coins += 35 # hour 3
    total_coins += 35 # hour 4 (before giving 15 away)
    total_coins -= 15 # hour 4 (after giving 15 away)
    result = total_coins
    return result

print(solution())