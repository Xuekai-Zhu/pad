def solution():
    # Calculate the total cost in gold
    spellbooks_cost = 5 * 5  # Five spellbooks that each cost 5 gold
    potion_kits_cost = 3 * 20 / 9  # Three potion kits that each cost 20 silver, converted to gold
    owl_cost = 28  # One owl that costs 28 gold
    total_cost_in_gold = spellbooks_cost + potion_kits_cost + owl_cost

    # Convert the total cost to silver
    total_cost_in_silver = total_cost_in_gold * 9  # 9 silver to a gold
    result = total_cost_in_silver
    return result

print(solution())