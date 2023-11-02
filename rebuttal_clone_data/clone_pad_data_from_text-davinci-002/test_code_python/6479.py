def solution():
    clay_pots = 80
    cracked_pots = 2/5 * clay_pots
    usable_pots = clay_pots - cracked_pots
    price_per_pot = 40
    money_made = usable_pots * price_per_pot
    result = money_made
    return result

print(solution())