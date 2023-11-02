def solution():
    """On a farm, on average every 6 cows produce 108 liters of milk per week. In five weeks the cows produced 2160 liters of milk. How many cows are on the farm?"""
    # Define the average milk production per cow per week
    milk_production_per_cow_per_week = 108/6

    # Calculate the total milk production for all cows in the farm for five weeks
    total_milk_production = 2160

    # Calculate the total number of cow-weeks needed to produce the total milk production
    total_cow_weeks = total_milk_production / milk_production_per_cow_per_week / 5

    # Calculate the total number of cows on the farm
    total_cows = total_cow_weeks / 5

    result = round(total_cows)
    return result

print(solution())