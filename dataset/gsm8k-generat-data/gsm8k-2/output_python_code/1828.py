def solution():
    """Harry needs to buy 5 spellbooks that each cost 5 gold, three potion kits that each cost 20 silver, and one owl that costs 28 gold. There are 9 silver to a gold. How much will Harry pay total, in silvers?"""
    spellbook_cost = 5 * 5  # 25 gold
    potion_cost = 3 * 20 / 9  # 6.67 gold or 60 silver
    owl_cost = 28 * 9  # 252 gold
    total_cost = spellbook_cost + potion_cost + owl_cost
    total_cost_in_silver = total_cost * 9
    result = total_cost_in_silver
    return result

print(solution())