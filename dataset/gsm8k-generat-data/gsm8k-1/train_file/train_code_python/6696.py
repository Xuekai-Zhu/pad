def solution():
    """Renne earns $4000 per month and wants to save half of her monthly earnings to buy the vehicle of her dreams worth $16000. How many months of saving will it take her to buy the vehicle?"""
    monthly_salary = 4000
    savings_percentage = 0.5
    vehicle_price = 16000
    savings_per_month = monthly_salary * savings_percentage
    months_to_save = vehicle_price / savings_per_month
    result = months_to_save
    return result

print(solution())