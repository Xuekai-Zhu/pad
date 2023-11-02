def solution():
    empty_fuel_rate = 20
    passenger_fuel_rate = 3
    bag_fuel_rate = 2
    distance = 400
    passengers = 30
    crew = 5
    bags_per_person = 2

    # Calculate the fuel rate per mile for all passengers and bags
    passenger_fuel_rate_total = (passengers + crew) * passenger_fuel_rate
    bag_fuel_rate_total = (passengers * bags_per_person) * bag_fuel_rate

    # Calculate the total fuel rate per mile
    total_fuel_rate = empty_fuel_rate + passenger_fuel_rate_total + bag_fuel_rate_total

    # Calculate the total amount of fuel needed for the trip
    total_fuel_needed = total_fuel_rate * distance
    result = total_fuel_needed
    return result

print(solution())