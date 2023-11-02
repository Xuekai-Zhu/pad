def solution():
    """Lucille made an agreement with her mom that she would earn six cents for every weed she pulled in her mom's garden. 
    There are eleven weeds in the flower bed, fourteen in the vegetable patch, and thirty-two in the grass around the fruit trees. 
    Lucille weeded the flower bed, the vegetable patch, and half the grass before she took a break. 
    She bought a soda for 99 cents on her break with some of her earnings. 
    How many cents does Lucille have left?"""
    # Define the payment per weed
    PAYMENT = 6
    
    # Calculate the number of weeds pulled in each area
    flowers_weeds = 11
    vegetable_weeds = 14
    half_grass_weeds = 32/2
    
    # Calculate the total number of weeds pulled
    total_weeds = flowers_weeds + vegetable_weeds + half_grass_weeds
    
    # Calculate Lucille's earnings
    earnings = total_weeds * PAYMENT
    
    # Subtract the cost of the soda
    remaining_money = earnings - 99
    
    # Display the remaining money in cents
    result = remaining_money
    return result

print(solution())