def solution():
    # Calculate the cost of the salads
    cost_salad = 3 * 2  # Two salads each costing $3

    # Calculate the cost of the beef
    cost_beef = 2 * (2 * 3)  # 2 kg of beef, with 1 kg costing 2 times the cost of one salad

    # Calculate the cost of the potatoes
    cost_potatoes = (1/3) * 3  # 1 kg of potatoes costing one-third the cost of one salad

    # Calculate the cost of the juice
    cost_juice = 1.5 * 2  # 2 liters of juice at $1.5 per liter

    # Calculate the total cost of all the ingredients
    total_cost = cost_salad + cost_beef + cost_potatoes + cost_juice
    result = total_cost
    return result

print(solution())