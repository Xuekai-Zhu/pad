def solution():
    """Tony, Moses and Esther are to share $50. Moses will take 40% of the total amount while Tony and Esther will split the remainder equally among themselves. How much more than Esther will Moses get?"""
    total_amount = 50
    moses_share = total_amount * 0.4
    remaining_amount = total_amount - moses_share
    tony_esther_share = remaining_amount / 2
    difference = moses_share - tony_esther_share
    result = difference
    return result

print(solution())