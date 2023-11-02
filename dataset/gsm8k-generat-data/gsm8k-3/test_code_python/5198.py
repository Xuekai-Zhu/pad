def solution():
    """Lisa was collecting socks to donate to a homeless shelter. She bought 12 pairs at a discount store. Sandra, her friend, came over and brought her 20 pairs of socks. Her cousin showed up with one-fifth the number of pairs that Sandra bought. After work, Lisa’s mom brought 8 more than three times the number of pairs Lisa started with. How many pairs of socks did Lisa end up with?"""
    # Define the initial number of pairs Lisa bought
    lisa_pairs = 12

    # Define the number of pairs Sandra brought
    sandra_pairs = 20

    # Define the number of pairs Lisa's cousin brought
    cousin_pairs = sandra_pairs // 5

    # Define the number of pairs Lisa's mom brought
    mom_pairs = 3 * lisa_pairs + 8

    # Calculate the total number of pairs Lisa ended up with
    total_pairs = lisa_pairs + sandra_pairs + cousin_pairs + mom_pairs

    # Display the total number of pairs Lisa ended up with
    result = total_pairs
    return result

print(solution())