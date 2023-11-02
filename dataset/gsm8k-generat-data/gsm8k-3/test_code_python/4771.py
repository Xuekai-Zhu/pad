def solution():
    """John rents a car to visit his family.  It cost $150 to rent the car.  He also had to buy 8 gallons of gas to fill it up and gas is $3.50 per gallon.  The final expense is $.50 per mile.  If he drove 320 miles how much did it cost?"""
    # Define the cost of gas per gallon
    GAS_PRICE = 3.5

    # Define the cost per mile
    MILE_PRICE = 0.5

    # Define the distance driven
    distance = 320

    # Calculate the cost of the gas
    gas_cost = 8 * GAS_PRICE

    # Calculate the cost of the miles driven
    miles_cost = distance * MILE_PRICE

    # Calculate the total cost
    total_cost = 150 + gas_cost + miles_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())