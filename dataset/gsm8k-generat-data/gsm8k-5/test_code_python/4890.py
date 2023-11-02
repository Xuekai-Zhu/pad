def solution():
    initial_mileage = 1728  # Marcus's car had 1728 miles on it before the road trip
    gas_tank_capacity = 20  # Marcus's car holds 20 gallons of gas
    miles_per_gallon = 30  # Marcus's car gets 30 miles per gallon

    # Calculate the total distance traveled on the trip
    total_distance_traveled = gas_tank_capacity * 2 * miles_per_gallon

    # Add the total distance traveled to the initial mileage to get the current mileage
    current_mileage = initial_mileage + total_distance_traveled
    result = current_mileage
    return result

print(solution())