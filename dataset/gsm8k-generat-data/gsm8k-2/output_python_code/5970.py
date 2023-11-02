def solution():
    """Matt can buy key chains in packs of 10 for $20 or in packs of 4 for $12.
    How much money can he save if he chooses to buy 20 key chains at a lower price?"""
    pack_of_10_price = 20
    pack_of_4_price = 12
    pack_of_10_quantity = 20 // 10
    remaining_keychains = 20 % 10
    total_pack_of_10_price = pack_of_10_quantity * pack_of_10_price
    if remaining_keychains:
        total_pack_of_10_price += pack_of_10_price
    pack_of_4_quantity = 20 // 4
    remaining_keychains = 20 % 4
    total_pack_of_4_price = pack_of_4_quantity * pack_of_4_price
    if remaining_keychains:
        total_pack_of_4_price += pack_of_4_price
    money_saved = total_pack_of_10_price - total_pack_of_4_price
    result = money_saved
    return result

print(solution())