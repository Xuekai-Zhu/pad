def solution():
    # Calculate the cost of oysters
    cost_oysters = 3 * 15  # 3 dozen oysters at $15.00 per dozen

    # Calculate the cost of shrimp
    cost_shrimp = 2 * 14  # 2 pounds of shrimp at $14.00 per pound

    # Calculate the cost of clams
    cost_clams = 2 * 13.5  # 2 pounds of clams at $13.50 per pound

    # Calculate the total cost
    total_cost = cost_oysters + cost_shrimp + cost_clams

    # Calculate the cost for each person
    cost_per_person = total_cost / 4

    result = cost_per_person
    return result

print(solution())