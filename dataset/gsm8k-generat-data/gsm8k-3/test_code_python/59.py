def solution():
    """Every hour Joanne has to collect the coins out of the fountain inside the mall. During the first hour, she collected 15 coins. For the next two hours, she collected 35 coins from the fountain. In the fourth hour, she collected 50 coins from the fountain but she gave 15 of them to her coworker so she could buy a soda. How many coins did she have after the fourth hour?"""
    # Define the number of coins collected in each hour
    hour1 = 15
    hour2 = 35
    hour3 = 35
    hour4 = 35 + 15

    # Calculate the total number of coins collected
    total_coins = hour1 + hour2 + hour3 + hour4 - 15

    # return the result
    result = total_coins
    return result

print(solution())