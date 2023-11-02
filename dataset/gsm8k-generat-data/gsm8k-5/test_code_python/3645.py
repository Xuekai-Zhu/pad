def solution():
    car_distance = 2 * 14  # Geordie's car travels 14 miles to work and back
    motorcycle_distance = 2 * 14  # Geordie's motorcycle also travels 14 miles to work and back
    car_gas_cost = (car_distance / 35) * 3.75  # Geordie's car uses 3.75 gallons of gas for the round trip
    motorcycle_gas_cost = (motorcycle_distance / 35) * 3.75  # Geordie's motorcycle uses 3.75 gallons of gas for the round trip
    car_toll_cost = 3 * 12.50  # Geordie's car uses the toll road three times a week, at a cost of $12.50 per use
    motorcycle_toll_cost = 2 * 7  # Geordie's motorcycle uses the toll road twice a week, at a cost of $7 per use

    # Calculate the total cost for driving to work and back in a week
    total_cost = car_gas_cost + motorcycle_gas_cost + car_toll_cost + motorcycle_toll_cost
    result = total_cost
    return result

print(solution())