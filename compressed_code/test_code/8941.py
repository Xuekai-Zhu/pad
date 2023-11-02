def solution():
    
    goats_bought = 3
    goat_price = 400
    llamas_bought = 2 * goats_bought
    llama_price = goat_price * 1.5
    total_spent = (goats_bought * goat_price) + (llamas_bought * llama_price)
    result = total_spent
    return result

print(solution())