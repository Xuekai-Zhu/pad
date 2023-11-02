def solution():
    """Maria has 4 dimes, 4 quarters, and 7 nickels in her piggy bank. Her mom gives her 5 quarters. How much money, in dollars, does Maria have now?"""
    dimes = 4
    quarters = 4 + 5
    nickels = 7
    total_cents = (dimes * 10) + (quarters * 25) + (nickels * 5)
    total_dollars = total_cents / 100
    result = total_dollars
    
    return result

print(solution())