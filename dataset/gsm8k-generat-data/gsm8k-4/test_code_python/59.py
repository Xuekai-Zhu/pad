def solution():
    """Every hour Joanne has to collect the coins out of the fountain inside the mall. During the first hour, she collected 15 coins. For the next two hours, she collected 35 coins from the fountain. In the fourth hour, she collected 50 coins from the fountain but she gave 15 of them to her coworker so she could buy a soda. How many coins did she have after the fourth hour?"""
    # Joanne collected 15 coins in the first hour
    total_coins = 15

    # Joanne collected 35 coins in the second and third hours
    total_coins += 35 * 2

    # Joanne collected 50 coins in the fourth hour, but gave away 15
    total_coins += 50 - 15

    result = total_coins
    return result

print(solution())