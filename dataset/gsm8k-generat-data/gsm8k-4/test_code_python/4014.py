def solution():
    """Adonis is playing a prank on his dad by replacing his shampoo with hot sauce.
    Every day, after his dad showers, Adonis replaces the shampoo with 1/2 an ounce of hot sauce.
    He knows his dad uses 1 oz of shampoo a day from a new 10 oz bottle that no one else uses.
    After 4 days, what percentage of the liquid in the bottle is hot sauce?"""
    
    # Define the volume of the shampoo bottle and the amount of hot sauce added each day
    shampoo_volume = 10
    hot_sauce_added = 0.5

    # Calculate the total amount of hot sauce added after 4 days
    total_hot_sauce_added = hot_sauce_added * 4

    # Calculate the total volume of liquid in the bottle after 4 days
    total_volume = shampoo_volume - 4 + total_hot_sauce_added

    # Calculate the percentage of the liquid that is hot sauce
    hot_sauce_percentage = (total_hot_sauce_added / total_volume) * 100

    # return the result
    result = hot_sauce_percentage
    return result

print(solution())