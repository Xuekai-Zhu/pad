def solution():
    # Calculate the total cost of gas for the road trip
    gas_prices = [3, 3.5, 4, 4.5]  # prices of gas at each of the 4 gas stations
    total_cost = 0  # initialize the total cost to zero
    for price in gas_prices:
        gallons_needed = 12  # Tara's car has a 12-gallon tank
        cost = price * gallons_needed
        total_cost += cost  # add the cost of gas at each gas station to the total cost
    result = total_cost
    return result

print(solution())