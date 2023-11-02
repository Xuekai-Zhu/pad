def solution():
    """Four friends ordered four pizzas for a total of 64 dollars. If two of the pizzas cost 30 dollars, how much did each of the other two pizzas cost if they cost the same amount?"""
    total_cost = 64
    cost_of_two_pizzas = 30
    remaining_cost = total_cost - cost_of_two_pizzas * 2
    cost_per_pizza = remaining_cost / 2
    result = cost_per_pizza
    return result

print(solution())