def solution():
    roses = 20  # Nadia was sent to buy 20 roses
    lilies = 3/4 * roses  # Nadia was also sent to buy 3/4 times as many Lillies as roses
    cost_roses = 5  # Roses cost $5 each
    cost_lilies = 2 * cost_roses  # Lilies cost twice as much as roses
    total_cost = (roses * cost_roses) + (lilies * cost_lilies)  # Calculate the total cost of the flowers

    result = total_cost
    return result

print(solution())