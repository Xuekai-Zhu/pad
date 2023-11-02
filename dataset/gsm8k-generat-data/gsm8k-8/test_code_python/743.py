def solution():
    empty_fuel = 20
    passenger_fuel = (30 + 5) * 3
    bag_fuel = (30 + 5) * 2 * 2
    total_fuel = empty_fuel + passenger_fuel + bag_fuel
    fuel_for_400_miles = total_fuel * 400
    result = fuel_for_400_miles
    return result

print(solution())