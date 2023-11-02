def solution():
    """Harry needs to buy 5 spellbooks that each cost 5 gold, three potion kits that each cost 20 silver, and one owl that costs 28 gold. There are 9 silver to a gold. How much will Harry pay total, in silvers?"""
    spellbook_cost = 5
    num_spellbooks = 5
    potion_cost = 20
    num_potions = 3
    owl_cost = 28
    gold_to_silver = 9
    
    total_cost = (spellbook_cost * num_spellbooks) + (potion_cost * num_potions) + (owl_cost * gold_to_silver)
    result = total_cost
    
    return result

print(solution())