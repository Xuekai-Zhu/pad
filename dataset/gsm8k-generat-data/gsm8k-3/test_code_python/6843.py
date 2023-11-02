def solution():
    """Sophie went to the Dunkin Donuts store and bought 4 boxes of donuts. There were 12 donuts in each box. She gave 1 box to her mom and half a dozen to her sister. How many donuts were left for her?"""
    # Define the number of boxes and donuts per box
    BOXES = 4
    DONUTS_PER_BOX = 12

    # Calculate the total number of donuts
    total_donuts = BOXES * DONUTS_PER_BOX

    # Calculate the number of donuts given away
    donuts_given_away = DONUTS_PER_BOX + 6

    # Calculate the number of donuts left for Sophie
    donuts_left = total_donuts - donuts_given_away

    # Display the number of donuts left for Sophie
    result = donuts_left
    return result

print(solution())