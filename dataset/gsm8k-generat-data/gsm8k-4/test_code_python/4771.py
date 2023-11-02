def solution():
    """John rents a car to visit his family.  It cost $150 to rent the car.  He also had to buy 8 gallons of gas to fill it up and gas is $3.50 per gallon.  The final expense is $.50 per mile.  If he drove 320 miles how much did it cost?"""
    # Define the initial cost of renting the car
    rental_cost = 150

    # Define the cost of gas
    gas_cost = 8 * 3.5

    # Define the cost of driving
    driving_cost = 0.5 * 320

    # Calculate the total cost
    total_cost = rental_cost + gas_cost + driving_cost

    # Return the result
    result = total_cost
    return result

print(solution())