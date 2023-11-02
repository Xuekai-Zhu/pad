def solution():
    """The cheese pizza is cut into 12 slices and the pepperoni pizza is cut into 8 slices. If Kate’s 6 friends each eat 6 cheese pizza slices and 4 pepperoni pizza slices, how many pizza pies does she need to buy?"""
    cheese_slices_per_pie = 12
    pepperoni_slices_per_pie = 8
    num_friends = 6
    cheese_slices_per_friend = 6
    pepperoni_slices_per_friend = 4
    total_cheese_slices = num_friends * cheese_slices_per_friend
    total_pepperoni_slices = num_friends * pepperoni_slices_per_friend
    total_pizza_slices = total_cheese_slices + total_pepperoni_slices
    total_pizzas = total_pizza_slices / (cheese_slices_per_pie + pepperoni_slices_per_pie)
    result = total_pizzas
    return result

print(solution())