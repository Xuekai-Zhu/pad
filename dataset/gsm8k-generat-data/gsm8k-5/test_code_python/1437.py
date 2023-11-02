def solution():
    # Calculate the area of the deck
    area = 30 * 40  # 30 feet by 40 feet

    # Calculate the cost of the deck without sealant
    cost_no_sealant = area * 3  # $3 per square foot

    # Calculate the cost of the sealant
    cost_sealant = area * 1  # $1 per square foot

    # Calculate the total cost
    total_cost = cost_no_sealant + cost_sealant
    result = total_cost
    return result

print(solution())