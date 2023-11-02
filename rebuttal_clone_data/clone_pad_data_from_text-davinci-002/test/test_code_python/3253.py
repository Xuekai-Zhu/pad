def solution():
     slices_per_pizza = 8
     pizzas_ordered = 3
     people = 12
     total_slices = slices_per_pizza * pizzas_ordered
     slices_per_person = total_slices / people
     result = slices_per_person
     return result

print(solution())