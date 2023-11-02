def solution():
    pizza_price = 14
    soda_price = 1.8

    hubert_pizza = 8
    hubert_soda = 10

    ian_pizza = 10
    ian_soda = 15

    # Calculate the total cost for Hubert
    hubert_total = (hubert_pizza * pizza_price) + (hubert_soda * soda_price)

    # Calculate the total cost for Ian
    ian_total = (ian_pizza * pizza_price) + (ian_soda * soda_price)

    # Calculate the total cost for the pizza party
    total_cost = hubert_total + ian_total
    result = total_cost
    return result

print(solution())