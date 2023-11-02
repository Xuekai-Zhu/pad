def solution():
    # Calculate the car's gas mileage
    gas_mileage = 400 / 20  # miles per gallon

    # Calculate the distance Mr. Montero's car can travel with 8 gallons of gas
    distance_with_8_gallons = gas_mileage * 8

    # Calculate the remaining distance Mr. Montero needs to travel
    remaining_distance = 600 - (2 * distance_with_8_gallons)

    # Calculate the additional amount of gas Mr. Montero needs
    additional_gas = remaining_distance / gas_mileage

    result = additional_gas
    return result

print(solution())