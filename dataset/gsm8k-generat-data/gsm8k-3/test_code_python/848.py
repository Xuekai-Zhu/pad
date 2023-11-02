def solution():
    """On a farm, on average every 6 cows produce 108 liters of milk per week. In five weeks the cows produced 2160 liters of milk. How many cows are on the farm?"""
    # Define the average weekly milk production per cow and the number of weeks
    AVG_MILK_PRODUCTION = 108
    WEEKS = 5

    # Calculate the total milk production over the 5 weeks
    total_milk_production = 2160

    # Calculate the total number of cows on the farm
    total_cows = (total_milk_production / (AVG_MILK_PRODUCTION * WEEKS)) * 6

    # Display the total number of cows on the farm
    result = total_cows
    return result

print(solution())