def solution():
    total_distance = 10 + 6 + 5 + 9  # Luisa drives a total distance of 30 miles
    gallons_needed = total_distance / 15  # Each gallon of gas covers 15 miles
    cost_per_gallon = 3.5  # One gallon of gas costs $3.50

    # Calculate the total cost of gas for Luisa's entire trip
    total_cost = gallons_needed * cost_per_gallon
    result = total_cost
    return result

print(solution())