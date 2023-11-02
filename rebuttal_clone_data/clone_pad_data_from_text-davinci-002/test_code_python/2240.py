def solution():
    total_cost = 55
    number_of_shrimp_trays = 5
    shrimp_tray_cost = 5
    total_shrimp_cost = number_of_shrimp_trays * shrimp_tray_cost
    remaining_cost = total_cost - total_shrimp_cost
    number_of_gum_packs = 2
    gum_pack_cost = remaining_cost / 2
    pint_cost = remaining_cost - (number_of_gum_packs * gum_pack_cost)
    result = pint_cost

    return result

print(solution())