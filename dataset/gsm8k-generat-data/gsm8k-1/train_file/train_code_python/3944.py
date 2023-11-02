def solution():
    """Nelly wants to buy pizza for herself and her 14 friends. Each pizza costs $12 and can feed 3 people. If Nelly earns $4 a night babysitting the neighbors' kids, how many nights will she have to babysit to afford the pizza?"""
    total_people = 1 + 14
    pizzas_needed = (total_people // 3) + (total_people % 3 > 0)
    cost_per_pizza = 12
    total_cost = pizzas_needed * cost_per_pizza
    nights_babysitting = total_cost // 4
    result = nights_babysitting
    return result

print(solution())