def solution():
    """Tara's taking a road trip for the weekend. She drives for two days, stopping to fill up her gas tank each time from empty to full when she needs it. She visits 4 different gas stations in total, with the price of gas being $3, $3.50, $4, and $4.50 respectively at each. If Tara's car has a 12-gallon tank, how much does she spend on gas for her road trip?"""
    # Define the tank capacity and the number of gas stops
    TANK_CAPACITY = 12
    NUM_GAS_STOPS = 2

    # Define the prices of gas at each stop
    GAS_PRICES = [3, 3.5, 4, 4.5]

    # Initialize the total cost of gas
    total_cost = 0

    # Calculate the cost of gas at each stop and add it to the total
    for i in range(NUM_GAS_STOPS):
        # Calculate the amount of gas needed to fill the tank
        gas_needed = TANK_CAPACITY

        # Select the gas station with the lowest price
        min_price = min(GAS_PRICES)
        min_index = GAS_PRICES.index(min_price)

        # Calculate the cost of gas at the selected station
        gas_cost = min_price * gas_needed

        # Add the cost to the total and remove the price from the list of gas prices
        total_cost += gas_cost
        del GAS_PRICES[min_index]

    result = total_cost
    return result

print(solution())