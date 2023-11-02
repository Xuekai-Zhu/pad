def solution():
    # Calculate the total number of pizzas needed
    total_pizzas = (14 + 1) // 3  # Nelly has 14 friends plus herself, and each pizza feeds 3 people

    # Calculate the total cost of the pizzas
    total_cost = total_pizzas * 12  # Each pizza costs $12

    # Calculate how many nights Nelly needs to babysit to afford the pizzas
    nights_of_babysitting = total_cost / 4  # Nelly earns $4 a night babysitting

    result = nights_of_babysitting
    return result

print(solution())