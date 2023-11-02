def solution():
    num_packs = 4
    grape_pack_price = 2
    new_pack_price = grape_pack_price / 2
    total_paid = 7

    # Calculate the total cost of all packs of gum
    total_gum_cost = num_packs * grape_pack_price + new_pack_price

    # Calculate the cost of each pack of strawberry gum
    cost_per_pack = total_gum_cost / strawberry_packs
    result = cost_per_pack
    return result

print(solution())