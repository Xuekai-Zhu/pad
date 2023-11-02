def solution():
    
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