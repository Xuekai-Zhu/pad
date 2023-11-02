def solution():
    """Tara's taking a road trip for the weekend.  She drives for two days, stopping to fill up her gas tank each time from empty to full when she needs it.  She visits 4 different gas stations in total, with the price of gas being $3, $3.50, $4, and $4.50 respectively at each.  If Tara's car has a 12-gallon tank, how much does she spend on gas for her road trip?"""
    # Define the size of Tara's gas tank
    gas_tank_size = 12

    # Define the prices of gas at each of the 4 gas stations
    gas_prices = [3, 3.5, 4, 4.5]

    # Define variables to keep track of the total amount of gas purchased and the total cost
    total_gas = 0
    total_cost = 0

    # Loop through the gas stations visited and calculate the amount of gas purchased and the cost
    for price in gas_prices:
        amount_of_gas = gas_tank_size - total_gas
        cost = amount_of_gas * price
        total_gas += amount_of_gas
        total_cost += cost

    # Display the total cost of gas
    result = total_cost
    return result

print(solution())