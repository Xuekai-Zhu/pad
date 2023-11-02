def solution():
    """Marie is planning to buy a new cash register for her bakery that costs $1040. 
    Every day Marie sells 40 loaves of bread for $2 each and 6 cakes for $12 each. 
    She has to pay $20 each day for rent and $2 each day for electricity. 
    How many days' worth of profits will it take for Marie to pay for the cash register?"""
    
    # Define the cost of the cash register
    cash_register_cost = 1040
    
    # Define the daily revenue and expenses
    daily_revenue = (40*2) + (6*12)
    daily_expenses = 20 + 2
    
    # Calculate the profit per day
    daily_profit = daily_revenue - daily_expenses
    
    # Calculate the number of days needed to pay for the cash register
    days_needed = cash_register_cost / daily_profit
    
    # Round up to the nearest whole number of days
    days_needed = math.ceil(days_needed)
    
    # Display the result
    result = days_needed
    return result

print(solution())