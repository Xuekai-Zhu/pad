def solution():
    
    slices_per_person = 12
    small_pizza_slices = 8
    large_pizza_slices = 14
    total_slices_needed = (slices_per_person * 3) - small_pizza_slices
    large_pizzas_needed = total_slices_needed // large_pizza_slices + \
        (1 if total_slices_needed %
         large_pizza_slices != 0 else 0)  
    result = large_pizzas_needed
    return result

print(solution())