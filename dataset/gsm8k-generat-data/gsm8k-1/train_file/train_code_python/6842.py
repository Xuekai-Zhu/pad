def solution():
    """Sophie went to the Dunkin Donuts store and bought 4 boxes of donuts. There were 12 donuts in each box. She gave 1 box to her mom and half a dozen to her sister. How many donuts were left for her?"""
    boxes_of_donuts = 4
    donuts_per_box = 12
    donuts_given_to_mom = donuts_per_box
    donuts_given_to_sister = 6
    total_donuts_given = donuts_given_to_mom + donuts_given_to_sister
    remaining_donuts = (boxes_of_donuts * donuts_per_box) - total_donuts_given
    result = remaining_donuts
    return result

print(solution())