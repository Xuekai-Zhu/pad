def solution():
    distance_per_trip = 150  # The trip is 150 kilometers long each way
    total_distance = distance_per_trip * 2  # The total distance they will travel in a day
    liters_per_trip = total_distance / 15  # They need 1 liter of gasoline for every 15 kilometers
    cost_per_trip = liters_per_trip * 0.9  # The cost of gasoline per trip

    # The cost of the first car rental option
    cost_option1 = 50 + cost_per_trip

    # The cost of the second car rental option
    cost_option2 = 90

    # Calculate the savings if they choose the first option
    savings = cost_option2 - cost_option1
    result = savings
    return result

print(solution())