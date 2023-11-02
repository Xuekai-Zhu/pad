def solution():
    """James buys 3 packs of candy. He pays with a $20 bill and gets $11 change. How much did each pack of candy cost?"""
    total_paid = 20 - 11
    num_packs = 3
    total_cost = total_paid / num_packs
    result = total_cost
    return result

print(solution())