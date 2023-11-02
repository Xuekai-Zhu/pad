def solution():
    """Susie babysits every day for 3 hours per day at the rate of $10 per hour. She spent 3/10 of the money she earned from last week to buy a make-up set. She then spent 2/5 of her money on her skincare products. How much is left from her earnings last week, in dollars?"""
    
    # Define the number of hours Susie babysits each day and her hourly rate
    hours_per_day = 3
    hourly_rate = 10
    
    # Calculate the total earnings for a week (7 days)
    total_earnings = hours_per_day * hourly_rate * 7
    
    # Calculate the amount spent on the make-up set
    makeup_spending = total_earnings * 0.3
    
    # Calculate the amount spent on skincare products
    skincare_spending = total_earnings * (2/5)
    
    # Calculate the remaining amount from her earnings
    remaining_earnings = total_earnings - makeup_spending - skincare_spending
    
    # return the result
    result = remaining_earnings
    return result

print(solution())