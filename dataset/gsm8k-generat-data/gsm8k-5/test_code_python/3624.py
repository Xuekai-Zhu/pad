def solution():
    fuel_efficiency = 3  # The semi-truck can go 3 miles per gallon of gas
    distance_to_cover = 90  # The cheaper gas station is 90 miles away
    current_fuel_level = 12  # The semi-truck already has 12 gallons of gas in its tank

    # Calculate how much fuel is needed to cover the remaining distance
    remaining_fuel_needed = (distance_to_cover / fuel_efficiency) - current_fuel_level
    result = remaining_fuel_needed
    return result

print(solution())