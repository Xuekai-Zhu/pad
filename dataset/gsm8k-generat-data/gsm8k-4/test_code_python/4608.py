def solution():
    """Juanita enters a drumming contest. It costs $10 to enter. She has 2 minutes to hit as many drums as she can. If she hits 200 drums, she can start to make money, equal to 2.5 cents for every drum hit. How many drums does she hit if she lost $7.5 for joining the contest?"""
    # Define the cost to enter the contest and the minimum number of drums to make a profit
    ENTRY_COST = 10
    MIN_DRUMS_FOR_PROFIT = 200

    # Define the profit per drum hit
    PROFIT_PER_DRUM_HIT = 0.025

    # Calculate the minimum earnings to break even
    minimum_earnings = ENTRY_COST - 7.5

    # Calculate how many drums Juanita needs to hi to break even
    drums_for_break_even = minimum_earnings / PROFIT_PER_DRUM_HIT

    # If Juanita hits fewer drums than required to break even, return 0
    if drums_for_break_even > MIN_DRUMS_FOR_PROFIT:
        drums_hit = drums_for_break_even
    else:
        drums_hit = 0

    result = drums_hit
    return result

print(solution())