def solution():
    money_given = 100  # Amy's grandfather gave her $100
    cost_per_doll = 1  # Each doll costs $1
    num_dolls_bought = 3  # Amy bought 3 dolls

    # Calculate the total cost of the dolls
    total_cost = cost_per_doll * num_dolls_bought

    # Calculate how much money Amy has left
    money_left = money_given - total_cost
    result = money_left
    return result

print(solution())