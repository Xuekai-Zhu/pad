def solution():
    """Judy uses 10 pencils during her 5 day school week. A 30 pack of pencils costs $4. How much will she spend on pencils over 45 days?"""
    pencils_per_day = 2
    days = 45
    pencils_per_pack = 30
    pack_price = 4
    total_pencils = pencils_per_day * days
    total_packs = (total_pencils // pencils_per_pack) + 1 # adding 1 to make sure enough packs are bought
    total_price = total_packs * pack_price
    result = total_price
    return result

print(solution())