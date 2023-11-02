def solution():
    # Calculate the total number of pizzas needed
    total_pizzas = (14 + 1) // 3  # add one to account for Nelly herself

    # Calculate the cost of the pizzas
    pizza_cost = total_pizzas * 12

    # Calculate the number of nights Nelly needs to babysit
    nights_babysitting = pizza_cost / 4  # Nelly earns $4 a night babysitting

    result = nights_babysitting
    return result

print(solution())