def solution():
    """Marly has ten $20 bills, eight $10 bills, and four $5 bills. If she wants to change her bills to $100 bills, how many pieces of $100 bills will she have?"""
    total_money = (10*20) + (8*10) + (4*5) # Total money in dollars
    num_100_bills = total_money // 100 # Number of $100 bills Marly will have
    result = num_100_bills
    return result

print(solution())