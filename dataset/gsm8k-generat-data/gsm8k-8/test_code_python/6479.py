def solution():
    total_pots = 80
    cracked_pots = (2/5) * total_pots
    usable_pots = total_pots - cracked_pots
    price_per_pot = 40
    income = usable_pots * price_per_pot
    result = income
    return result

print(solution())