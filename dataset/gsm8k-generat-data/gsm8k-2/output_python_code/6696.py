def solution():
    """Renne earns $4000 per month and wants to save half of her monthly earnings to buy the vehicle of her dreams worth $16000. How many months of saving will it take her to buy the vehicle?"""
    monthly_earnings = 4000
    monthly_savings = monthly_earnings / 2
    vehicle_cost = 16000
    saving_time = vehicle_cost / monthly_savings
    result = saving_time
    return result

print(solution())