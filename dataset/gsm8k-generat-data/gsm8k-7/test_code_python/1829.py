def solution():
    num_spellbooks = 5
    spellbook_cost = 5

    num_potion_kits = 3
    potion_kit_cost = 20

    owl_cost = 28

    silver_per_gold = 9

    # Calculate the total cost of all spellbooks
    total_spellbook_cost = num_spellbooks * spellbook_cost

    # Calculate the total cost of all potion kits, converting to gold first
    total_potion_kit_cost = (num_potion_kits * potion_kit_cost) / silver_per_gold

    # Calculate the total cost of the owl, adding to the gold total
    total_owl_cost = owl_cost

    # Calculate the total cost in gold
    total_gold_cost = total_spellbook_cost + total_potion_kit_cost + total_owl_cost

    # Convert the gold cost to silver
    total_silver_cost = total_gold_cost * silver_per_gold
    result = total_silver_cost
    return result

print(solution())