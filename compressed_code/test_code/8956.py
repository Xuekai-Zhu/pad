def solution():
    
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