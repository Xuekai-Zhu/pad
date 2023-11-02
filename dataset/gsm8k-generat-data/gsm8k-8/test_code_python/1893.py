def solution():
    # Define the payment rate and gas cost
    payment_rate = 0.5
    gas_cost = 4

    # Calculate the gas used in the trip
    gas_used = 600/20

    # Calculate the cost of gas for the trip
    gas_cost_trip = gas_used * gas_cost

    # Calculate the profit from the trip
    profit = (600 * payment_rate) - gas_cost_trip

    result = profit
    return result

print(solution())