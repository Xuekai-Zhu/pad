def solution():
    # Calculate the total cost of the goats
    goat_cost = 3 * 400

    # Calculate the cost per llama
    llama_cost = 1.5 * 400

    # Calculate the number of llamas Tim bought
    llama_count = 2 * 3

    # Calculate the total cost of the llamas
    llama_total_cost = llama_cost * llama_count

    # Calculate the total amount Tim spent
    total_cost = goat_cost + llama_total_cost
    result = total_cost
    return result

print(solution())