def solution():
    """Tim drinks 2 bottles that are each 1.5 quarts and an additional 20 ounces a day. How much water does he drink a week?"""
    # Define the amount of water Tim drinks per day
    bottles_per_day = 2
    bottle_size = 1.5 # in quarts
    additional_water = 20/32 # convert ounces to quarts
    total_water_per_day = bottles_per_day * bottle_size + additional_water

    # Calculate the amount of water Tim drinks per week
    water_per_week = total_water_per_day * 7

    result = round(water_per_week, 2)
    return result

print(solution())