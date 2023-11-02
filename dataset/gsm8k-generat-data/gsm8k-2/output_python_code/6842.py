def solution():
    """Sophie went to the Dunkin Donuts store and bought 4 boxes of donuts. There were 12 donuts in each box. She gave 1 box to her mom and half a dozen to her sister. How many donuts were left for her?"""
    total_donuts = 4 * 12
    mom_donuts = 12
    sister_donuts = 6
    remaining_donuts = total_donuts - mom_donuts - sister_donuts
    result = remaining_donuts
    return result

print(solution())