def solution():
    # Cost of buying 3 goats at $400 each
    cost_goats = 3 * 400

    # Cost of buying twice as many llamas as goats
    num_llamas = 2 * 3  # Twice as many llamas as goats
    cost_llama = 1.5 * 400  # Llamas cost 50% more than goats
    cost_llamas = num_llamas * cost_llama

    # Total cost
    total_cost = cost_goats + cost_llamas
    result = total_cost
    return result

print(solution())