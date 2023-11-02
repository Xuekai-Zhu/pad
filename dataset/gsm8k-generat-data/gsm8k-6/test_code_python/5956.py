def solution():
    # Calculate the cost of gasoline they need for their trip
    gas_needed = (150 * 2) / 15  # 150 kilometers each way, 1 liter of gasoline can cover 15 kilometers
    gas_cost = gas_needed * 0.90  # $0.90 per liter of gasoline

    # Calculate the total cost of renting the first option car
    first_option_rental_cost = 50 + gas_cost

    # Calculate the total cost of renting the second option car
    second_option_rental_cost = 90

    # Calculate the difference between the two options
    savings = second_option_rental_cost - first_option_rental_cost
    result = savings
    return result

print(solution())