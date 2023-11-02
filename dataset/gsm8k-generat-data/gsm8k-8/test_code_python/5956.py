def solution():
    # Calculate the total distance of the trip
    total_distance = 150 * 2

    # Calculate the amount of gasoline needed in liters
    gasoline_needed = total_distance / 15

    # Calculate the cost of gasoline needed
    gasoline_cost = gasoline_needed * 0.90

    # Calculate the total cost of the first option
    first_option_cost = 50 + gasoline_cost

    # Calculate the total cost of the second option
    second_option_cost = 90

    # Calculate the savings by choosing the first option
    savings = second_option_cost - first_option_cost
    result = savings
    return result

print(solution())