def solution():
    spellbooks = 5
    spellbook_cost = 5
    potion_kits = 3
    potion_kit_cost = 20
    owls = 1
    owl_cost = 28
    total_gold_cost = spellbooks * spellbook_cost + potion_kits * potion_kit_cost + owls * owl_cost
    total_silver_cost = total_gold_cost * 9
    result = total_silver_cost
    
    return result

print(solution())