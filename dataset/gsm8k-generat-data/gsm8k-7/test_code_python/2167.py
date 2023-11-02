def solution():
    gas_cost_per_gallon = 2.0
    miles_per_gallon = 10.0
    driving_rate = 30.0
    pay_per_mile = 0.5
    driving_time = 10.0

    # Calculate the total distance driven
    total_distance = driving_rate * driving_time

    # Calculate the total gallons of gas used
    total_gas = total_distance / miles_per_gallon

    # Calculate the total cost of gas used
    total_gas_cost = total_gas * gas_cost_per_gallon

    # Calculate the total earnings from driving
    total_earnings = total_distance * pay_per_mile

    # Calculate the total profit (earnings minus gas cost)
    total_profit = total_earnings - total_gas_cost
    result = total_profit
    return result

print(solution())