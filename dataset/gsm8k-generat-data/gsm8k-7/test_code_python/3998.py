def solution():
    num_goats = 3
    goat_price = 400

    num_llamas = num_goats * 2
    llama_price = goat_price * 1.5

    # Calculate the total cost of all goats
    total_goat_cost = num_goats * goat_price

    # Calculate the total cost of all llamas
    total_llama_cost = num_llamas * llama_price

    # Calculate the total cost of all animals
    total_cost = total_goat_cost + total_llama_cost
    result = total_cost
    return result

print(solution())