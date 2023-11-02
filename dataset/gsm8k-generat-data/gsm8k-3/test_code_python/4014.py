def solution():
    """Adonis is playing a prank on his dad by replacing his shampoo with hot sauce. Every day, after his dad showers, Adonis replaces the shampoo with 1/2 an ounce of hot sauce. He knows his dad uses 1 oz of shampoo a day from a new 10 oz bottle that no one else uses. After 4 days, what percentage of the liquid in the bottle is hot sauce?"""
    # Define the amount of shampoo and hot sauce used each day
    SHAMPOO_USED = 1
    HOTSAUCE_USED = 0.5

    # Calculate the amount of shampoo and hot sauce used over 4 days
    total_shampoo_used = SHAMPOO_USED * 4
    total_hotsauce_used = HOTSAUCE_USED * 4

    # Calculate the amount of liquid left in the bottle
    total_liquid_left = 10 - total_shampoo_used

    # Calculate the percentage of hot sauce in the remaining liquid
    hot_sauce_percent = (total_hotsauce_used / total_liquid_left) * 100

    # Display the percentage of hot sauce in the remaining liquid
    result = hot_sauce_percent
    return result

print(solution())