def solution():
    mpg = 25
    miles_driven = 50
    days_driven = 5
    tank_size = 10
    weeks_to_drive = 4
    total_miles_driven = miles_driven * days_driven * weeks_to_drive
    total_gallons_used = total_miles_driven / mpg
    gas_cost = 2
    total_cost = total_gallons_used * gas_cost
    result = total_cost
    return result

print(solution())