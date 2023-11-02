def solution():
    # Calculate the total cost of the shrimp and gum
    shrimp_cost = 5 * 5  # cost of 5 trays of jumbo shrimp
    gum_cost = 2 * 0.5 * pint_cost  # cost of 2 packs of chewing gum

    # Calculate the cost of 5 pints of frozen yogurt
    total_cost = 55 - shrimp_cost - gum_cost  # total cost of everything except the frozen yogurt
    pint_cost = total_cost / 5

    result = pint_cost
    return result

print(solution())