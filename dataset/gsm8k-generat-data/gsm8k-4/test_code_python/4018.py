def solution():
    """Two friends, Hubert and Ian, are planning to have a pizza party. One box of pizza is worth $14, and a can of soda is worth $1.80. Hubert orders eight boxes of pizza and ten cans of soda. Ian buys ten boxes of pizza and fifteen cans of soda. How much do they spend in all?"""
    # Define the prices of pizza and soda
    pizza_price = 14
    soda_price = 1.8

    # Calculate the total cost of pizza and soda for Hubert
    hubert_pizza_cost = 8 * pizza_price
    hubert_soda_cost = 10 * soda_price

    # Calculate the total cost of pizza and soda for Ian
    ian_pizza_cost = 10 * pizza_price
    ian_soda_cost = 15 * soda_price

    # Calculate the total cost of the party
    total_cost = hubert_pizza_cost + hubert_soda_cost + ian_pizza_cost + ian_soda_cost

    result = total_cost
    return result

print(solution())