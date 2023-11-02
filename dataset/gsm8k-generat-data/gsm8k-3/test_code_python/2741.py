def solution():
    """Zoe wants to go on the field trip to Washington DC with her middle school this spring and the cost is $485. Her grandma gave her $250 toward her fees and she must earn the rest by selling candy bars. She makes $1.25 for every candy bar she sells. How many candy bars does Zoe need to sell to earn the money for the trip?"""
    # Define the total cost of the field trip
    TRIP_COST = 485

    # Define the amount of money Zoe was given
    GRANDMA_MONEY = 250

    # Calculate the amount of money Zoe needs to earn
    money_needed = TRIP_COST - GRANDMA_MONEY

    # Calculate the number of candy bars Zoe needs to sell
    candy_bars_needed = int(money_needed / 1.25)

    # Display the number of candy bars Zoe needs to sell
    result = candy_bars_needed
    return result

print(solution())