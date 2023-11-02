def solution():
    # Calculate the cost of each item
    cost_salad = 3
    cost_beef = 2 * cost_salad
    cost_potatoes = cost_salad / 3
    cost_juice = 1.5

    # Calculate the total cost of all the items purchased
    total_cost = (2 * cost_salad) + (2 * cost_beef) + (1 * cost_potatoes) + (2 * cost_juice)

    result = total_cost
    return result

print(solution())