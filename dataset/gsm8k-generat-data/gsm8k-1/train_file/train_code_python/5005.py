def solution():
    """James buys 3 packs of candy. He pays with a $20 bill and gets $11 change. How much did each pack of candy cost?"""
    num_packs = 3
    total_paid = 20 - 11
    cost_per_pack = total_paid / num_packs
    result = cost_per_pack
    return result

print(solution())