def solution():
    """Two friends, Hubert and Ian, are planning to have a pizza party. One box of pizza is worth $14, and a can of soda is worth $1.80. Hubert orders eight boxes of pizza and ten cans of soda. Ian buys ten boxes of pizza and fifteen cans of soda. How much do they spend in all?"""
    pizza_price = 14
    soda_price = 1.8
    
    hubert_pizzas = 8
    hubert_sodas = 10
    hubert_total = (hubert_pizzas * pizza_price) + (hubert_sodas * soda_price)
    
    ian_pizzas = 10
    ian_sodas = 15
    ian_total = (ian_pizzas * pizza_price) + (ian_sodas * soda_price)
    
    total_spent = hubert_total + ian_total
    result = total_spent
    return result

print(solution())