def solution():
    """If Beth had $35 more, she would have $105. If Jan had $10 less, he would have the same money as Beth has. How much money do Beth and Jan have altogether?"""
    
    # Let x be the amount of money Beth has
    # Let y be the amount of money Jan has
    
    # From the first statement we have:
    # x + 35 = 105
    x = 70
    
    # From the second statement we have:
    # y - 10 = x
    y = x + 10
    
    # Total amount of money they have together
    total_money = x + y
    
    # Display total amount of money
    result = total_money
    return result

print(solution())