def solution():
    cost_of_parking = 10
    cost_of_ticket = 55
    cost_of_meal_pass = 25
    distance = 165
    fuel_efficiency = 30  # miles per gallon
    cost_of_gas_per_gallon = 3

    total_cost = cost_of_parking + cost_of_ticket + cost_of_meal_pass
    gallons_required = distance / fuel_efficiency
    cost_of_gas = gallons_required * cost_of_gas_per_gallon

    total_cost += cost_of_gas
    remaining_amount = total_cost - 28
    result = remaining_amount
    return result

print(solution())