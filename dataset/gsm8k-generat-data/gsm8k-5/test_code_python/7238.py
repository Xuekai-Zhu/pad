def solution():
    miles_per_day = 2.5 * 8  # The man can hike 2.5 miles per hour and hikes for 8 hours per day
    total_miles = miles_per_day * 5  # The man is hiking for 5 days
    supplies_per_mile = 0.5  # The man needs to pack 0.5 pounds of supplies per mile
    initial_supplies = total_miles * supplies_per_mile  # The man needs to bring this amount of supplies with his first pack
    resupply_ratio = 0.25  # The resupply will be 25% as large as the first pack
    resupply = initial_supplies * resupply_ratio  # The man will get this amount of supplies during his resupply
    total_supplies = initial_supplies + resupply  # The man will have this total amount of supplies during his hike
    result = total_supplies
    return result

print(solution())