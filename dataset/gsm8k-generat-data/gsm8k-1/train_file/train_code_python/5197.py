def solution():
    """Lisa was collecting socks to donate to a homeless shelter. She bought 12 pairs at a discount store. Sandra, her friend, came over and brought her 20 pairs of socks. Her cousin showed up with one-fifth the number of pairs that Sandra bought. After work, Lisa’s mom brought 8 more than three times the number of pairs Lisa started with. How many pairs of socks did Lisa end up with?"""
    lisa_bought = 12
    sandra_brought = 20
    cousin_brought = sandra_brought / 5
    moms_socks = (lisa_bought * 3) + 8
    total_socks = lisa_bought + sandra_brought + cousin_brought + moms_socks
    result = total_socks
    return result

print(solution())