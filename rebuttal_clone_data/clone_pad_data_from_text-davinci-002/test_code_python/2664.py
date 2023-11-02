def solution():
    pizzas = 4
    pizza_slices = 12
    eaten_slices = 39
    left_over_slices = pizzas * pizza_slices - eaten_slices
    result = left_over_slices
    return result

print(solution())