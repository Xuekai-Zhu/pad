def solution():
    """Vanessa wants to buy a dress she saw at the mall, which costs $80, and she already has $20 in savings. Her parents give her $30 every week, but she also spends $10 each weekend at the arcades. How many weeks will she have to wait until she can gather enough money to buy the dress?"""
    cost_of_dress = 80
    current_savings = 20
    weekly_allowance = 30
    weekly_spending = 10
    money_needed = cost_of_dress - current_savings
    weeks_needed = (money_needed + weekly_allowance - 1) // weekly_allowance
    weeks_spent = weeks_needed * weekly_spending
    result = weeks_needed + (weeks_spent // 7)
    return result

print(solution())