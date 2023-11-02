def solution():
    hubert_pizza = 8
    ian_pizza = 10
    price_of_pizza = 14
    hubert_soda = 10
    ian_soda = 15
    price_of_soda = 1.80
    hubert_total = hubert_pizza * price_of_pizza + hubert_soda * price_of_soda
    ian_total = ian_pizza * price_of_pizza + ian_soda * price_of_soda
    result = hubert_total + ian_total
    return result

print(solution())