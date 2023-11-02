def solution():
    """Tony drives a car that gets 25 miles to the gallon.  He drives 50 miles round trip to work 5 days a week.  His tank holds 10 gallons.  He begins the week with a full tank and when he runs out he fills up at the local gas station for $2 a gallon.  How much money does Tony spend on gas in 4 weeks?"""
    # Define the variables
    MPG = 25
    DISTANCE = 50
    WORK_DAYS = 5
    TANK_SIZE = 10
    GAS_PRICE = 2
    WEEKS = 4

    # Calculate the distance driven in one day
    daily_distance = DISTANCE * 2

    # Calculate the daily gas usage
    daily_gas_usage = daily_distance / MPG

    # Calculate the weekly gas usage
    weekly_gas_usage = daily_gas_usage * WORK_DAYS

    # Calculate the amount of gas needed per week
    gas_per_week = weekly_gas_usage / TANK_SIZE

    # Calculate the cost of gas per week
    cost_per_week = gas_per_week * TANK_SIZE * GAS_PRICE

    # Calculate the total cost of gas for 4 weeks
    total_cost = cost_per_week * WEEKS

    # Display the total cost of gas
    result = total_cost
    return result

print(solution())