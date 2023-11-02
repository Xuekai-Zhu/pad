def solution():
    """Vanessa wants to buy a dress she saw at the mall, which costs $80,
    and she already has $20 in savings. Her parents give her $30 every week,
    but she also spends $10 each weekend at the arcades. How many weeks will
    she have to wait until she can gather enough money to buy the dress?"""
    dress_price = 80
    savings = 20
    weekly_allowance = 30
    weekly_spending = 10
    remaining_price = dress_price - savings
    weeks_to_save = 0
    while remaining_price > 0:
        weeks_to_save += 1
        remaining_price -= (weekly_allowance - weekly_spending)
    result = weeks_to_save
    return result

print(solution())