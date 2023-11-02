def solution():
    miles_driven_mon_wed_fri = 50
    miles_driven_sun = 100
    total_miles_driven = (miles_driven_mon_wed_fri * 3) + (miles_driven_sun * 4)
    cost_per_mile = 0.1
    total_cost = total_miles_driven * cost_per_mile + (100 * 52)
    result = total_cost
    return result

print(solution())