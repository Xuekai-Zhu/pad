def solution():
    """A car uses 20 gallons of gas to travel 400 miles. Mr. Montero's car has 8 gallons in it. How many more gallons of gas does he need to travel 600 miles, back and forth?"""
    # Calculate the rate of fuel consumption (gallons per mile)
    fuel_rate = 20 / 400

    # Calculate the distance Mr. Montero's car can travel with the gas it has
    distance_with_current_gas = fuel_rate * 8

    # Calculate the additional distance Mr. Montero needs to travel (600 - the distance he can travel with current gas)
    additional_distance = 600 - distance_with_current_gas

    # Calculate the additional fuel needed to travel the additional distance
    additional_fuel = additional_distance / fuel_rate

    # Calculate the total fuel needed (to travel back and forth)
    total_fuel_needed = additional_fuel * 2

    # Display the total fuel needed
    result = total_fuel_needed
    return result

print(solution())