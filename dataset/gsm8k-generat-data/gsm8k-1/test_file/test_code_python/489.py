def solution():
    """Heather's razors come 4 to a pack and cost $4.00 a pack. They are currently on sale for buy one get one free. She also has a $2.00 coupon. How much will each individual razor cost, in cents, after the discount if she buys 2 packs of razors?"""
    razors_per_pack = 4
    pack_cost = 4
    packs_bought = 2
    discount = pack_cost * (packs_bought / 2) + 2
    total_cost = pack_cost * packs_bought - discount
    total_razors = razors_per_pack * packs_bought
    cost_per_razor = total_cost / total_razors * 100
    result = cost_per_razor
    return result

print(solution())