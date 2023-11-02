def solution():
    """A car uses 20 gallons of gas to travel 400 miles. Mr. Montero's car has 8 gallons in it. How many more gallons of gas does he need to travel 600 miles, back and forth?"""
    car_miles_per_gallon = 20
    initial_gas = 8
    target_miles = 600
    one_way_distance = target_miles / 2
    one_way_gallons = one_way_distance / car_miles_per_gallon
    total_gallons = initial_gas + one_way_gallons
    result = total_gallons
    return result

print(solution())