def solution():
    
    goat_price = 400
    num_goats = 3
    llama_price = 1.5 * goat_price
    num_llamas = 2 * num_goats
    total_cost = (goat_price * num_goats) + (llama_price * num_llamas)
    result = total_cost
    return result

print(solution())