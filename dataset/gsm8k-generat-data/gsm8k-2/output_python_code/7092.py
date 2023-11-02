def solution():
    """Carl is having a party on Saturday and is inviting 15 guests. He would like to make sure everyone, including himself, has at least 2 glasses of punch. Each glass holds 12 ounces of punch. How many ounces of punch does he need to buy for the party?"""
    total_glasses = 2 * 16 # 15 guests + Carl
    punch_ounces_per_glass = 12
    total_ounces = total_glasses * punch_ounces_per_glass
    result = total_ounces
    return result

print(solution())