def solution():
    """Mark has $50 in his bank account. He earns $10 per day at his work. If he wants to buy a bike that costs $300, how many days does Mark have to save his money?"""
    starting_balance = 50
    bike_cost = 300
    daily_income = 10
    days_to_save = (bike_cost - starting_balance) / daily_income
    result = days_to_save
    return result

print(solution())