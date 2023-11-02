def solution():
    """Adonis is playing a prank on his dad by replacing his shampoo with hot sauce. 
    Every day, after his dad showers, Adonis replaces the shampoo with 1/2 an ounce of hot sauce. 
    He knows his dad uses 1 oz of shampoo a day from a new 10 oz bottle that no one else uses. 
    After 4 days, what percentage of the liquid in the bottle is hot sauce?"""
    
    shampoo_per_day = 1
    hot_sauce_per_day = 0.5
    total_bottle_size = 10
    days = 4
    
    total_shampoo_used = shampoo_per_day * days
    total_hot_sauce_used = hot_sauce_per_day * days
    
    percentage_hot_sauce = (total_hot_sauce_used / (total_shampoo_used + total_hot_sauce_used)) * 100
    
    result = percentage_hot_sauce
    
    return result

print(solution())