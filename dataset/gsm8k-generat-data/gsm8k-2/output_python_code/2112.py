def solution():
    """Tina decides to fill a jar with coins. In the first hour she puts in 20 coins. During the next two hours she puts in 30 coins each time. During the fourth hour she puts in 40 coins. During the fifth hour her mother asks to borrow some money so she takes 20 coins out. How many coins are left after the fifth hour?"""
    total_coins = 20 + 30*2 + 40
    remaining_coins = total_coins - 20
    result = remaining_coins
    return result

print(solution())