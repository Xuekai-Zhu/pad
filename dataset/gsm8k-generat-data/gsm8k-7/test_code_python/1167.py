def solution():
    total_amount_of_potatoes = 5
    cost_of_2_kg_of_potatoes = 6

    # Calculate the cost of 1 kg of potatoes
    cost_of_1_kg_of_potatoes = cost_of_2_kg_of_potatoes / 2

    # Calculate the total cost of 5 kg of potatoes
    total_cost = total_amount_of_potatoes * cost_of_1_kg_of_potatoes
    result = total_cost
    return result

print(solution())