def solution():
    """Rica's group won in a dance competition. She got 3/8 of the prize money. From Rica's prize money,
    she spent 1/5 of it and is now left with $300. How much was the prize money that her group won?"""
    
    # Let's assume the total prize money as x
    # From the problem, Rica got 3/8 of the prize money, so her prize money would be (3/8) * x
    
    rica_prize_money = (3/8) * x
    
    # Now, we know that Rica spent 1/5 of her prize money and is left with $300, so we can calculate her initial prize money
    
    rica_initial_prize_money = rica_prize_money / (1 - 1/5)
    
    # We also know that Rica's initial prize money is equal to $300 plus the amount she spent, so we can calculate the total prize money as
    
    x = rica_initial_prize_money + rica_prize_money
    
    result = x
    return result

print(solution())