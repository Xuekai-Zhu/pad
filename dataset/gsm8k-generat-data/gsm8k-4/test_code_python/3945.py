def solution():
    """Nelly wants to buy pizza for herself and her 14 friends. Each pizza costs $12 and can feed 3 people. If Nelly earns $4 a night babysitting the neighbors' kids, how many nights will she have to babysit to afford the pizza?"""
    # Define the number of people to feed and the cost per pizza
    people_to_feed = 15
    pizza_cost = 12
   
    # Calculate the number of pizzas needed to feed everyone
    pizzas_needed = (people_to_feed // 3) + (1 if people_to_feed % 3 > 0 else 0)

    # Calculate the total cost of the pizzas
    total_cost = pizzas_needed * pizza_cost

    # Calculate the number of nights Nelly needs to babysit to afford the pizzas
    nights_needed = total_cost / 4

    # Round up the number of nights to the nearest integer
    nights_needed = int(nights_needed) + (1 if nights_needed % 1 > 0 else 0)

    result = nights_needed
    return result

print(solution())