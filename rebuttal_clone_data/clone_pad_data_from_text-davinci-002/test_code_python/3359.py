def solution():
     total_slices_needed = 36
     slices_in_small_pizza = 8
     slices_in_large_pizza = 14
     small_pizzas_needed = 1
     large_pizzas_needed = (total_slices_needed - (slices_in_small_pizza * small_pizzas_needed)) / slices_in_large_pizza
     result = large_pizzas_needed
     return result

print(solution())