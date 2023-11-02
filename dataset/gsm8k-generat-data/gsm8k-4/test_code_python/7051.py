def solution():
    """Jane is dividing up minnows to be carnival prizes. She bought 600 minnows, and each prize is a bowl with 3 minnows. If 800 people are going to play the game and 15% win a prize, how many minnows will be left over?"""
    # Define the initial number of minnows
    initial_minnows = 600

    # Define the number of people who win a prize
    winners = round(800 * 0.15)

    # Define the number of minnows needed for the prizes
    prize_minnows = winners * 3

    # Calculate the number of minnows left over
    leftover_minnows = initial_minnows - prize_minnows

    # Return the result
    result = leftover_minnows
    return result

print(solution())