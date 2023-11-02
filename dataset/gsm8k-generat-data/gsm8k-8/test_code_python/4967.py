def solution():
    # Calculate the number of gallons lost during the first 5 hours
    water_lost_5_hours = 32000 * 5

    # Calculate the number of gallons lost during the next 10 hours
    water_lost_10_hours = 10000 * 10

    # Calculate the total amount of water lost before repairs
    total_water_lost = water_lost_5_hours + water_lost_10_hours

    # Calculate the number of gallons added during repairs
    water_added_during_repairs = 40000 * 3

    # Calculate the remaining capacity of the tank after repairs
    remaining_capacity = 350000 - total_water_lost + water_added_during_repairs

    # Calculate the number of missing gallons for the tank to be at maximum capacity
    missing_gallons = 350000 - remaining_capacity

    result = missing_gallons
    return result

print(solution())