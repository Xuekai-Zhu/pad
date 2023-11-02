def solution():
    """A truck driver has to spend $2 per gallon of gas. She can drive 10 miles per gallon. She drives at a rate of 30 miles per hour. If she is paid $.50 per mile, how much money does she make if she drives for 10 hours?"""
    # Define the cost of gas per gallon and the miles per gallon
    GAS_PRICE = 2
    MILES_PER_GALLON = 10

    # Define the driver's speed in miles per hour and the pay rate per mile
    SPEED = 30
    PAY_RATE = 0.5

    # Define the number of hours the driver will work
    hours_worked = 10

    # Calculate the total distance the driver can cover in 10 hours
    total_distance = SPEED * hours_worked

    # Calculate the total number of gallons of gas needed to cover the distance
    gas_needed = total_distance / MILES_PER_GALLON

    # Calculate the cost of the gas needed
    gas_cost = gas_needed * GAS_PRICE

    # Calculate the total earnings of the driver
    earnings = total_distance * PAY_RATE

    # Calculate the net profit of the driver
    net_profit = earnings - gas_cost

    result = net_profit
    return result

print(solution())