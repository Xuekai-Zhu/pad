def solution():
    """TreShawn's mom needs to order pizza for her son and his two friends. She knows that TreShawn always eats 1/2 a pizza. His friend Michael eats 1/3 of a pizza and his other friend LaMar eats 1/6 of a pizza. How many pizzas does she need to order?"""
    treshawn_slices = 0.5
    michael_slices = 1/3
    lamar_slices = 1/6
    total_slices = treshawn_slices + michael_slices + lamar_slices
    pizzas = total_slices / 8  # there are 8 slices per pizza
    result = pizzas
    return result

print(solution())