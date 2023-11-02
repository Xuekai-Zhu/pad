def solution():
    """Two friends, Hubert and Ian, are planning to have a pizza party. One box of pizza is worth $14, and a can of soda is worth $1.80. Hubert orders eight boxes of pizza and ten cans of soda. Ian buys ten boxes of pizza and fifteen cans of soda. How much do they spend in all?"""
    pizza_price = 14
    soda_price = 1.8
    hubert_pizza = 8
    hubert_soda = 10
    ian_pizza = 10
    ian_soda = 15

    hubert_total = (hubert_pizza * pizza_price) + (hubert_soda * soda_price)
    ian_total = (ian_pizza * pizza_price) + (ian_soda * soda_price)

    total_spent = hubert_total + ian_total
    result = total_spent
    return result

print(solution())