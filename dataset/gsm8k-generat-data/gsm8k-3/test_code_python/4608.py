def solution():
    """Juanita enters a drumming contest. It costs $10 to enter. She has 2 minutes to hit as many drums as she can. If she hits 200 drums, she can start to make money, equal to 2.5 cents for every drum hit. How many drums does she hit if she lost $7.5 for joining the contest?"""
    # Define the cost to enter the contest and the earnings per drum hit
    ENTRY_FEE = 10
    EARNINGS_PER_DRUM_HIT = 0.025

    # Define the amount Juanita lost, i.e. her total cost minus her total earnings
    total_loss = 7.5

    # Calculate the total cost, i.e. the entry fee plus the amount lost
    total_cost = ENTRY_FEE + total_loss

    # Calculate the number of drums Juanita hit to make enough money to cover the cost
    drums_needed = total_cost / EARNINGS_PER_DRUM_HIT - 200

    # Display the number of drums Juanita hit
    result = int(drums_needed)
    return result

print(solution())