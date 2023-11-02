def solution():
    # Calculate the total cost of Dakota's hospital stay
    bed_cost = 900 * 3  # $900/day for 3 days in the hospital
    specialist_cost = (250 * 4) * 2  # $250/hour for 2 specialists for 15 minutes each, for 4 times a day
    ambulance_cost = 1800  # $1800 for the ambulance ride
    total_cost = bed_cost + specialist_cost + ambulance_cost
    result = total_cost
    return result

print(solution())