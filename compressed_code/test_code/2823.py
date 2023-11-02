def solution():
    
    small_pizza_slices = 4
    large_pizza_slices = 8
    small_pizzas = 3
    large_pizzas = 2
    george_slices = 3
    bob_slices = george_slices + 1
    susie_slices = bob_slices / 2
    bill_slices = 3
    fred_slices = 3
    mark_slices = 3

    total_slices = (small_pizzas * small_pizza_slices) + (large_pizzas * large_pizza_slices)
    total_slices -= (george_slices + bob_slices + susie_slices + bill_slices + fred_slices + mark_slices)
    result = total_slices
    return result

print(solution())