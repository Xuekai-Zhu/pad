def solution():
    # Calculate the total cost of the oysters, shrimp, and clams
    cost_oysters = 3 * 15  # 3 dozen oysters at $15 per dozen
    cost_shrimp = 2 * 14  # 2 pounds of shrimp at $14 per pound
    cost_clams = 2 * 13.5  # 2 pounds of clams at $13.50 per pound
    total_cost = cost_oysters + cost_shrimp + cost_clams

    # Calculate the cost per person
    cost_per_person = total_cost / 4
    result = cost_per_person
    return result

print(solution())