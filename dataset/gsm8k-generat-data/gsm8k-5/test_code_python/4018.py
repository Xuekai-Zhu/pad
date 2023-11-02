def solution():
    pizza_cost = 14  # Cost of one box of pizza
    soda_cost = 1.8  # Cost of one can of soda

    # Cost of Hubert's order
    hubert_pizza_cost = pizza_cost * 8
    hubert_soda_cost = soda_cost * 10
    hubert_total_cost = hubert_pizza_cost + hubert_soda_cost

    # Cost of Ian's order
    ian_pizza_cost = pizza_cost * 10
    ian_soda_cost = soda_cost * 15
    ian_total_cost = ian_pizza_cost + ian_soda_cost

    # Total cost for both of them
    total_cost = hubert_total_cost + ian_total_cost
    result = total_cost
    return result

print(solution())