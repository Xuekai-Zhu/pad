def solution():
    """Tina decides to fill a jar with coins. In the first hour she puts in 20 coins. During the next two hours she puts in 30 coins each time. During the fourth hour she puts in 40 coins. During the fifth hour her mother asks to borrow some money so she takes 20 coins out. How many coins are left after the fifth hour?"""
    # Initialize the number of coins in the jar
    coins = 20

    # Add the coins Tina puts in during the second and third hours
    coins += 30 + 30

    # Add the coins Tina puts in during the fourth hour
    coins += 40

    # Remove the coins Tina's mother borrows during the fifth hour
    coins -= 20

    # The number of coins left after the fifth hour is the final amount
    result = coins
    return result

print(solution())