def solution():
    initial_savings = 28
    park_cost = 10
    entrance_cost = 55
    meal_cost = 25
    gas_cost = 3
    trip_distance = 165
    gas_efficiency = 30
    gallons_of_gas = trip_distance / gas_efficiency
    total_gas_cost = gallons_of_gas * gas_cost
    total_trip_cost = total_gas_cost + park_cost + entrance_cost + meal_cost
    money_needed = total_trip_cost - initial_savings
    result = money_needed
    return result

print(solution())