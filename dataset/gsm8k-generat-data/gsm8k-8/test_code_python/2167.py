def solution():
    # Calculate the total distance the truck driver can cover in 10 hours
    total_distance = 10 * 30

    # Calculate the total amount of gas the truck driver needs for the trip
    total_gas = total_distance / 10

    # Calculate the total cost of the gas
    gas_cost = total_gas * 2

    # Calculate the money the truck driver makes from driving
    driving_income = total_distance * 0.5

    # Calculate the total profit
    total_profit = driving_income - gas_cost

    # Return the total profit
    result = total_profit
    return result

print(solution())