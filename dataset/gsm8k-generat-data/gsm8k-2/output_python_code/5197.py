def solution():
    """Lisa was collecting socks to donate to a homeless shelter. She bought 12 pairs at a discount store. Sandra, her friend, came over and brought her 20 pairs of socks. Her cousin showed up with one-fifth the number of pairs that Sandra bought. After work, Lisa’s mom brought 8 more than three times the number of pairs Lisa started with. How many pairs of socks did Lisa end up with?"""
    lisa_start = 12
    sandra = 20
    cousin = sandra / 5
    mom = 8 + 3 * lisa_start
    total_socks = lisa_start + sandra + cousin + mom
    result = total_socks
    return result

print(solution())