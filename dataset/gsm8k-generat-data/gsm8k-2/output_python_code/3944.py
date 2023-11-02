def solution():
    """Nelly wants to buy pizza for herself and her 14 friends. Each pizza costs $12 and can feed 3 people. If Nelly earns $4 a night babysitting the neighbors' kids, how many nights will she have to babysit to afford the pizza?"""
    num_people = 15
    num_pizzas = (num_people // 3) + (num_people % 3 > 0)
    pizza_cost = 12
    total_cost = num_pizzas * pizza_cost
    babysitting_income = 4
    num_nights = total_cost / babysitting_income
    result = round(num_nights)
    return result

print(solution())