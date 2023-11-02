def solution():
    """Cheyenne is a craftswoman making pots for sale. On a particular week, she made 80 clay pots. However, when she put them in the sun to dry, 2/5 of the pots cracked and could not be sold. How much money did Cheyenne make from selling the remaining items at $40 per clay pot?"""
    total_pots = 80
    cracked_pots = (2/5) * total_pots
    good_pots = total_pots - cracked_pots
    price_per_pot = 40
    income = good_pots * price_per_pot
    result = income
    return result

print(solution())