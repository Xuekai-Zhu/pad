def solution():
    """Luigi bought four pizzas for $80. Each pizza was cut into 5 pieces. How much did each piece of pizza cost, in dollars?"""
    num_pizzas = 4
    total_cost = 80
    num_slices = num_pizzas * 5
    cost_per_slice = total_cost / num_slices
    result = cost_per_slice
    return result

print(solution())