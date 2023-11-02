def solution():
     pizzas = 3
     slices_per_pizza = 8
     total_slices = pizzas * slices_per_pizza
     people = 5
     slices_per_person = total_slices / people
     result = slices_per_person
     return result

print(solution())