def solution():
    """Carson runs a carpool for five of his friends. The five of them cover all the gas expenses to compensate Carson for his time. Their total commute is 21 miles one way, gas costs $2.50/gallon, Carson's car gets 30 miles/gallon, and they commute to work 5 days a week, 4 weeks a month. How much does each person pay toward gas monthly?"""
    # Define the constants
    ONE_WAY_DISTANCE = 21
    GAS_COST = 2.5
    CAR_MPG = 30
    COMMUTE_DAYS_PER_MONTH = 5 * 4

    # Calculate the total distance covered by the carpool per month
    total_distance = ONE_WAY_DISTANCE * 2 * COMMUTE_DAYS_PER_MONTH

    # Calculate the total amount of gas needed per month
    total_gas = total_distance / CAR_MPG

    # Calculate the amount of gas each person needs to pay for per month
    gas_per_person = total_gas / 5

    # Calculate the cost of gas per person per month
    cost_per_person = gas_per_person * GAS_COST

    # Display the amount each person needs to pay
    result = cost_per_person
    return result

print(solution())