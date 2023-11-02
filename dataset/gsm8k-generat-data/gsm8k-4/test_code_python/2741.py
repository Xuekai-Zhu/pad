def solution():
    """Zoe wants to go on the field trip to Washington DC with her middle school this spring and the cost is $485. Her grandma gave her $250 toward her fees and she must earn the rest by selling candy bars. She makes $1.25 for every candy bar she sells. How many candy bars does Zoe need to sell to earn the money for the trip?"""
    # Define the cost of the field trip and the amount of money Zoe has already
    TRIP_COST = 485
    GRANDMA_MONEY = 250

    # Calculate how much money Zoe needs to earn
    remaining_money = TRIP_COST - GRANDMA_MONEY

    # Calculate how many candy bars she needs to sell to earn the remaining money
    candy_bars_needed = remaining_money / 1.25

    # Round up the number of candy bars needed to the nearest integer
    candy_bars_needed = round(candy_bars_needed)

    # Return the result
    result = candy_bars_needed
    return result

print(solution())