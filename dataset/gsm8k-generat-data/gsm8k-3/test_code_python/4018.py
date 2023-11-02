def solution():
    """Two friends, Hubert and Ian, are planning to have a pizza party. One box of pizza is worth $14, and a can of soda is worth $1.80. Hubert orders eight boxes of pizza and ten cans of soda. Ian buys ten boxes of pizza and fifteen cans of soda. How much do they spend in all?"""
    # Define the prices per item
    PIZZA_PRICE = 14
    SODA_PRICE = 1.8

    # Define the number of items ordered by each person
    hubert_pizzas = 8
    hubert_sodas = 10
    ian_pizzas = 10
    ian_sodas = 15

    # Calculate the total cost of Hubert's order
    hubert_cost = hubert_pizzas * PIZZA_PRICE + hubert_sodas * SODA_PRICE

    # Calculate the total cost of Ian's order
    ian_cost = ian_pizzas * PIZZA_PRICE + ian_sodas * SODA_PRICE

    # Calculate the total cost of both orders
    total_cost = hubert_cost + ian_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())