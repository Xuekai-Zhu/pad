def solution():
    """Nelly wants to buy pizza for herself and her 14 friends. Each pizza costs $12 and can feed 3 people. If Nelly earns $4 a night babysitting the neighbors' kids, how many nights will she have to babysit to afford the pizza?"""
    # Define the cost and feeding capacity of each pizza
    PIZZA_COST = 12
    PIZZA_FEEDS = 3

    # Calculate the total number of pizzas needed
    total_people = 1 + 14  # Nelly + her friends
    total_pizzas = (total_people // PIZZA_FEEDS) + (1 if total_people % PIZZA_FEEDS != 0 else 0)

    # Calculate the total cost of the pizzas
    total_cost = total_pizzas * PIZZA_COST

    # Calculate the number of nights Nelly needs to babysit to afford the pizzas
    nights_babysitting = total_cost // 4

    # Display the number of nights
    result = nights_babysitting
    return result

print(solution())