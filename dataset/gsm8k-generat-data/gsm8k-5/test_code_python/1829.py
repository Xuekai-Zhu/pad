def solution():
    # Calculate the cost of the spellbooks in gold
    spellbooks_cost = 5 * 5  # 5 spellbooks that each cost 5 gold

    # Calculate the cost of the potion kits in gold
    potion_kits_cost = 3 * 20 * 9 / 100  # 3 potion kits that each cost 20 silver, where 9 silver = 1 gold

    # Calculate the cost of the owl in gold
    owl_cost = 28

    # Calculate the total cost in gold
    total_cost_gold = spellbooks_cost + potion_kits_cost + owl_cost

    # Convert the total cost to silvers
    total_cost_silver = total_cost_gold * 9  # 1 gold = 9 silver

    result = total_cost_silver
    return result

print(solution())