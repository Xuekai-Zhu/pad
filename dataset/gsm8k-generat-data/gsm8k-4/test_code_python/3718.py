def solution():
    """Tom opens an amusement park. It cost $100,000 to open initially. It also cost 1% of that to run per day. He sells 150 tickets a day for $10 each. How long will it take to make back his money?"""
    # Define the initial cost to open the amusement park and the daily running cost
    INITIAL_COST = 100000
    DAILY_RUNNING_COST = INITIAL_COST * 0.01

    # Define the ticket price and the number of tickets sold per day
    TICKET_PRICE = 10
    TICKETS_SOLD_PER_DAY = 150

    # Initialize the day counter and the total earnings
    days = 0
    total_earnings = 0

    # Calculate the total cost of running the amusement park for each day
    daily_cost = DAILY_RUNNING_COST

    # Calculate the earnings from ticket sales each day, until the total earnings exceed the initial cost
    while total_earnings < INITIAL_COST:
        # Increment the day counter
        days += 1

        # Calculate the earnings from ticket sales
        ticket_earnings = TICKET_PRICE * TICKETS_SOLD_PER_DAY

        # Add the earnings to the total
        total_earnings += ticket_earnings

        # Subtract the daily cost from the total earnings
        total_earnings -= daily_cost

    # Display the number of days it took to make back the initial cost
    result = days
    return result

print(solution())