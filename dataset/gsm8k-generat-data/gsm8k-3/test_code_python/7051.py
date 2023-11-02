def solution():
    """Jane is dividing up minnows to be carnival prizes. She bought 600 minnows, and each prize is a bowl with 3 minnows. If 800 people are going to play the game and 15% win a prize, how many minnows will be left over?"""
    # Calculate the number of people who win a prize
    num_winners = round(800 * 0.15)

    # Calculate the number of minnows needed for the prizes
    minnows_for_prizes = num_winners * 3

    # Calculate the number of minnows left over
    minnows_left = 600 - minnows_for_prizes

    # Display the number of minnows left over
    result = minnows_left
    return result

print(solution())