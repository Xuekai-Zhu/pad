def solution():
    """Caden has four jars of coins. One jar of pennies, one jar of nickels, one jar of dimes and one jar of quarters. He has twice as many quarters as he does dimes. He has five times as many nickels as he does dimes. He has three times as many pennies as he does nickels. If he has 120 pennies, how much money does he have?"""
    penny_jar = 120
    nickel_jar = penny_jar * 3
    dime_jar = nickel_jar // 5
    quarter_jar = 2 * dime_jar
    total_money = penny_jar * 0.01 + nickel_jar * 0.05 + dime_jar * 0.1 + quarter_jar * 0.25
    result = total_money
    return result

print(solution())