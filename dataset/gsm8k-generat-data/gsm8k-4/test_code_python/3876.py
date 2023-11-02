def solution():
    """On Thursday the Meat Market sold 210kg of ground beef. On Friday they sold twice that amount. On Saturday they only sold 130kg. On Sunday they sold half of what they sold Saturday. If they originally planned to sell only 500kg, how much meat did they sell beyond their original plans?"""
    # Define the initial planned amount of meat to sell
    planned_amount = 500
    
    # Calculate the actual amount of meat sold each day
    thursday_amount = 210
    friday_amount = thursday_amount * 2
    saturday_amount = 130
    sunday_amount = saturday_amount / 2
    
    # Calculate the total amount of meat sold
    total_amount = thursday_amount + friday_amount + saturday_amount + sunday_amount
    
    # Calculate the amount of meat sold beyond the original plans
    extra_amount = total_amount - planned_amount
    
    # Return the result
    result = extra_amount
    return result

print(solution())