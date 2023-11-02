def solution():
    """Caden has four jars of coins. One jar of pennies, one jar of nickels, one jar of dimes and one jar of quarters. He has twice as many quarters as he does dimes. He has five times as many nickels as he does dimes. He has three times as many pennies as he does nickels. If he has 120 pennies, how much money does he have?"""
    pennies = 120
    nickels = pennies * 3
    dimes = nickels / 5
    quarters = dimes * 2
    total_cents = pennies + nickels * 5 + dimes * 10 + quarters * 25
    dollars = total_cents / 100
    result = dollars
    return result

print(solution())