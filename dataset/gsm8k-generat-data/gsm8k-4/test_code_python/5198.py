def solution():
    """Lisa was collecting socks to donate to a homeless shelter. She bought 12 pairs at a discount store. Sandra, her friend, came over and brought her 20 pairs of socks. Her cousin showed up with one-fifth the number of pairs that Sandra bought. After work, Lisa’s mom brought 8 more than three times the number of pairs Lisa started with. How many pairs of socks did Lisa end up with?"""
    # Define the number of pairs Lisa started with
    starting_pairs = 12

    # Define the number of pairs brought by Sandra
    sandra_pairs = 20

    # Define the number of pairs brought by Sandra's cousin
    cousin_pairs = sandra_pairs * 1/5

    # Define the number of pairs Lisa's mom brought
    mom_pairs = 8 + 3 * starting_pairs

    # Calculate the total number of pairs Lisa ended up with
    total_pairs = starting_pairs + sandra_pairs + cousin_pairs + mom_pairs

    # return the result
    result = total_pairs
    return result

print(solution())