def solution():
    """Albert is wondering how much pizza he can eat in one day. He buys 2 large pizzas and 2 small pizzas. A large pizza has 16 slices and a small pizza has 8 slices. If he eats it all, how many pieces does he eat that day?"""
    large_pizza_slices = 16
    small_pizza_slices = 8
    total_slices = (2 * large_pizza_slices * 2) + (2 * small_pizza_slices * 2)
    result = total_slices
    return result

print(solution())