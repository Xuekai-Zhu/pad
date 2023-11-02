def solution():
    """Fred wants to order a variety pack of sliced meats for the upcoming game. He can order a 4 pack of fancy, sliced meat for $40.00 and add rush delivery for an additional 30%. With rush shipping added, how much will each type of sliced meat cost?"""
    pack_price = 40.00
    rush_shipping = 0.3
    total_price = pack_price * (1 + rush_shipping)
    cost_per_type = total_price / 4
    result = cost_per_type
    return result

print(solution())