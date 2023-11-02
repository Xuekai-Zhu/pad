def solution():
    # Define the cost of one box of pizza and one can of soda
    pizza_cost = 14
    soda_cost = 1.8

    # Calculate the total cost of Hubert's order
    hubert_pizza_cost = pizza_cost * 8
    hubert_soda_cost = soda_cost * 10
    hubert_total_cost = hubert_pizza_cost + hubert_soda_cost

    # Calculate the total cost of Ian's order
    ian_pizza_cost = pizza_cost * 10
    ian_soda_cost = soda_cost * 15
    ian_total_cost = ian_pizza_cost + ian_soda_cost

    # Calculate the total cost
    total_cost = hubert_total_cost + ian_total_cost
    result = total_cost
    return result

print(solution())