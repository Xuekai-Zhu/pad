def solution():
    distance = 150
    gas_coverage_per_liter = 15
    gas_price_per_liter = 0.9

    # Calculate the total amount of gasoline needed for the trip
    total_gas_needed = (distance * 2) / gas_coverage_per_liter

    # Calculate the cost of gasoline for the trip
    gas_cost = total_gas_needed * gas_price_per_liter

    # Calculate the cost of the first rental option
    rental_option_1 = 50 + gas_cost

    # Calculate the cost of the second rental option
    rental_option_2 = 90

    # Calculate the savings if they choose the first option
    savings = rental_option_2 - rental_option_1
    result = savings
    return result

print(solution())