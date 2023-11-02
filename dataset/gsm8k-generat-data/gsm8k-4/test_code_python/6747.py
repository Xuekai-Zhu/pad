def solution():
    """Carson runs a carpool for five of his friends. The five of them cover all the gas expenses to compensate Carson for his time. Their total commute is 21 miles one way, gas costs $2.50/gallon, Carson's car gets 30 miles/gallon, and they commute to work 5 days a week, 4 weeks a month. How much does each person pay toward gas monthly?"""
    # Define the total distance traveled and the gas cost per gallon
    distance = 21 * 2  # round trip
    gas_cost = 2.5

    # Define the car's gas mileage and the number of commuters
    gas_mileage = 30
    num_commuters = 5

    # Calculate the total gas used for a single trip
    gas_used = distance / gas_mileage

    # Calculate the total gas cost for a single trip
    gas_total_cost = gas_used * gas_cost

    # Calculate the total gas cost for one person for a week
    weekly_gas_cost = gas_total_cost / num_commuters

    # Calculate the total gas cost for one person for a month
    monthly_gas_cost = weekly_gas_cost * 4

    # return the result
    result = monthly_gas_cost
    return result

print(solution())