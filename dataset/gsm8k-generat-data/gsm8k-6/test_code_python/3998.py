def solution():
    # Calculate the cost of 3 goats at $400 each
    goats_cost = 3 * 400  

    # Calculate the cost of each llama
    llama_cost = 1.5 * 400  # 50% more than the cost of a goat

    # Calculate the number of llamas Tim bought
    llamas_bought = 2 * 3  # twice as many llamas as goats

    # Calculate the cost of the llamas
    llamas_cost = llamas_bought * llama_cost

    # Calculate the total amount spent by Tim
    total_spent = goats_cost + llamas_cost

    result = total_spent
    return result

print(solution())