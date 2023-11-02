def solution():
    num_lollipops = 4
    lollipop_cost = 1.5

    num_gummies_packs = 2
    gummies_pack_cost = 2

    total_spent = (num_lollipops * lollipop_cost) + (num_gummies_packs * gummies_pack_cost)

    money_left = 15 - total_spent
    result = money_left
    return result

print(solution())