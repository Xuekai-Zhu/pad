def solution():
    # Calculate the total cost of the spellbooks
    spellbooks_cost = 5 * 5

    # Calculate the total cost of the potion kits
    potion_kits_cost = 3 * 20 * 9 # 9 silver to a gold

    # Calculate the total cost of the owl
    owl_cost = 28 * 9 # 9 silver to a gold

    # Calculate the total cost in silvers
    total_cost = spellbooks_cost + potion_kits_cost + owl_cost

    result = total_cost
    return result

print(solution())