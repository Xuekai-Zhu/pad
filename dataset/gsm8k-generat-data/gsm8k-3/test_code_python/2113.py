def solution():
    """Tina decides to fill a jar with coins. In the first hour she puts in 20 coins. During the next two hours she puts in 30 coins each time. During the fourth hour she puts in 40 coins. During the fifth hour her mother asks to borrow some money so she takes 20 coins out. How many coins are left after the fifth hour?"""
    # Define the number of coins Tina puts in during each hour
    coins_per_hour = [20, 30, 30, 40, -20]

    # Calculate the total number of coins
    total_coins = sum(coins_per_hour)

    # Display the total number of coins
    result = total_coins
    return result

print(solution())