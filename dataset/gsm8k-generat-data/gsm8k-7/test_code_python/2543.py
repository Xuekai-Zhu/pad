def solution():
    glasses_per_day = 4
    glass_size_ounces = 5
    water_bottle_size_ounces = 35
    days_per_week = 7

    # Calculate the total amount of water Matthew drinks per week
    total_water_weekly = glasses_per_day * glass_size_ounces * days_per_week

    # Calculate how many times he needs to refill the water bottle
    num_refills = total_water_weekly / water_bottle_size_ounces
    result = num_refills
    return result

print(solution())