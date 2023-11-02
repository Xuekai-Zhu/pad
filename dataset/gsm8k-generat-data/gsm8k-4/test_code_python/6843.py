def solution():
    """Sophie went to the Dunkin Donuts store and bought 4 boxes of donuts. There were 12 donuts in each box. She gave 1 box to her mom and half a dozen to her sister. How many donuts were left for her?"""
    # Define the initial number of donuts
    initial_donuts = 4 * 12

    # Subtract the number of donuts in the box she gave to her mom
    mom_donuts = 12
    remaining_donuts = initial_donuts - mom_donuts * 12

    # Subtract the number of donuts she gave to her sister (which is half a dozen or 6 donuts)
    sister_donuts = 6
    remaining_donuts = remaining_donuts - sister_donuts

    # Return the number of donuts left for Sophie
    result = remaining_donuts
    return result

print(solution())