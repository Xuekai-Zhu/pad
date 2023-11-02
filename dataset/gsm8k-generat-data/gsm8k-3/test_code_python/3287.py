def solution():
    """Jason is hiring two construction workers, one electrician and one plumber. If the construction workers each make $100/day, the electrician makes double what a worker is paid and the plumber makes 250% of a worker's salary, how much are the overall labor costs for one day?"""
    # Define the daily rate for workers, electrician, and plumber
    DAILY_RATE = 100
    ELECTRICIAN_RATE = DAILY_RATE * 2
    PLUMBER_RATE = DAILY_RATE * 2.5

    # Calculate the total labor cost for one day
    labor_cost = (DAILY_RATE * 2) + ELECTRICIAN_RATE + PLUMBER_RATE

    # Display the total labor cost for one day
    result = labor_cost
    return result

print(solution())