def solution():
    """Jason has a carriage house that he rents out. He’s charging $50.00 per day or $500.00 for 14 days. Eric wants to rent the house for 20 days. How much will it cost him?"""
    daily_rental_price = 50
    two_week_rental_price = 500
    days_in_two_weeks = 14
    additional_days = 20 - days_in_two_weeks
    
    if additional_days <= 0:
        total_cost = two_week_rental_price
    else:
        additional_cost = additional_days * daily_rental_price
        total_cost = two_week_rental_price + additional_cost
    
    result = total_cost
    return result

print(solution())