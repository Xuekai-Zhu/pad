def solution():
    """Fred wants to order a variety pack of sliced meats for the upcoming game. He can order a 4 pack of fancy, sliced meat for $40.00 and add rush delivery for an additional 30%. With rush shipping added, how much will each type of sliced meat cost?"""
    original_price = 40
    pack_size = 4
    total_price = original_price * 1.3
    price_per_type = total_price / pack_size
    result = price_per_type
    return result

print(solution())