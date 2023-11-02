def solution():
    base_charge = 3
    charge_per_mile = 4
    total_charge = 23
    miles_traveled = (total_charge - base_charge) / charge_per_mile
    result = miles_traveled
    return result

print(solution())