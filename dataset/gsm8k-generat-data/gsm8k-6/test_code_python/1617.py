def solution():
    # Calculate the cost of ingredients for one sandwich
    cost_of_bread = 0.15
    cost_of_ham = 0.25
    cost_of_cheese = 0.35
    total_cost = cost_of_bread + cost_of_ham + cost_of_cheese

    # Convert total cost to cents
    cost_in_cents = total_cost * 100
    result = int(cost_in_cents)
    return result

print(solution())