def solution():
    # Calculate the number of pizzas needed
    num_pizzas = 5  # (15 people total / 3 people per pizza = 5 pizzas)

    # Calculate the total cost of the pizzas
    pizza_cost = num_pizzas * 12

    # Calculate the amount of money Nelly needs to earn
    money_needed = pizza_cost - 4  # Nelly already has $4 from babysitting

    # Calculate the number of nights Nelly needs to babysit
    nights_needed = money_needed / 4  # Nelly earns $4 per night babysitting

    result = nights_needed
    return result

print(solution())