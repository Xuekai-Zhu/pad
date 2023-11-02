def solution():
    """A store offers a $2 discount for every $10 purchase on any item in the store. Kataleya went to the store and bought 400 peaches sold at forty cents each.
    Calculate the total amount of money she paid at the store for the fruits."""
    
    # Define the cost of each peach and the number of peaches purchased
    peach_cost = 0.40
    num_peaches = 400
    
    # Calculate the total cost of the peaches before any discount
    total_cost = peach_cost * num_peaches
    
    # Calculate the number of $10 purchases based on the total cost
    num_discounts = total_cost // 10
    
    # Calculate the total discount based on the number of discounts
    total_discount = num_discounts * 2
    
    # Calculate the final cost after applying the discount
    final_cost = total_cost - total_discount
    
    # Return the final cost rounded to 2 decimal places
    result = round(final_cost, 2)
    return result

print(solution())