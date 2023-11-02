def solution():
    total_allowance = 9 + 9  # Lola and Dora combined their allowance, which is $9 each
    total_spent = 10 + 2  # They spent $10 on playing cards and $2 on boxes of stickers
    remaining_allowance = total_allowance - total_spent  # They have $remaining_allowance left to buy stickers
    cost_per_pack = 1  # The cost per pack of stickers is $1
    packs_bought = remaining_allowance // cost_per_pack  # They split the cost evenly
    packs_for_dora = packs_bought // 2  # Dora gets half of the packs

    result = packs_for_dora
    return result

print(solution())