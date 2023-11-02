def solution():
    """Matthew drinks 4 glasses of water per day. Each glass is 5 ounces. He decides to just buy a 35 ounces water bottle. How many times will he fill it each week?"""
    # Define the number of glasses of water Matthew drinks per day and the size of his water bottle
    GLASSES_PER_DAY = 4
    GLASS_SIZE = 5 # in ounces
    BOTTLE_SIZE = 35 # in ounces

    # Calculate the total number of ounces of water Matthew drinks per day
    total_ounces_per_day = GLASSES_PER_DAY * GLASS_SIZE

    # Calculate the number of times Matthew will need to fill his water bottle each day
    fills_per_day = total_ounces_per_day / BOTTLE_SIZE

    # Calculate the number of times Matthew will need to fill his water bottle each week
    fills_per_week = fills_per_day * 7

    # Display the number of times Matthew will need to fill his water bottle each week
    result = fills_per_week
    return result

print(solution())