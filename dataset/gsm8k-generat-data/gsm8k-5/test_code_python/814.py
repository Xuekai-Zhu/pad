def solution():
    cost_croissants = 2 * 4.5  # Sean picks up 2 croissants every Sunday, at a cost of $4.50 each
    cost_plain_croissant = 3.0  # Sean also picks up a plain croissant for $3.00
    cost_focaccia = 4.0  # Sean picks up a loaf of focaccia for $4.00
    cost_lattes = 2 * 2.5  # Sean picks up 2 lattes for $2.50 each

    # Calculate the total cost of Sean's purchase
    total_cost = cost_croissants + cost_plain_croissant + cost_focaccia + cost_lattes

    result = total_cost
    return result

print(solution())