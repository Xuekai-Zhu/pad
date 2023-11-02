def solution():
    """A truck driver has to spend $2 per gallon of gas. She can drive 10 miles per gallon. She drives at a rate of 30 miles per hour. If she is paid $.50 per mile, how much money does she make if she drives for 10 hours?"""
    # Define the cost of gas per gallon and the driver's speed
    GAS_COST = 2
    SPEED = 30

    # Define the truck's fuel efficiency
    FUEL_EFFICIENCY = 10 # miles per gallon

    # Define the driver's pay rate per mile
    PAY_RATE = 0.5

    # Define the amount of time the driver will be driving
    time = 10 # hours

    # Calculate the total distance the driver will travel
    distance = SPEED * time

    # Calculate the total amount of gas the driver will need
    gas = distance / FUEL_EFFICIENCY

    # Calculate the total cost of the gas
    gas_cost = gas * GAS_COST

    # Calculate the total amount the driver will be paid
    pay = distance * PAY_RATE

    # Calculate the driver's profit
    profit = pay - gas_cost

    # Display the driver's profit
    result = profit
    return result

print(solution())