def solution():
    # Let x be Beth's current money and y be Jan's current money
    # From the first statement:
    x + 35 = 105 
    x = 70
    
    # From the second statement:
    y - 10 = x
    y = x + 10
    y = 80

    # Total money:
    total_money = x + y
    result = total_money
    return result

print(solution())