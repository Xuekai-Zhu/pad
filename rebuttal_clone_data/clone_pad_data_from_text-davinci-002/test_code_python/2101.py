def solution():
     people = 10
     slices_per_person = 2
     slices_per_pizza = 4
     pizzas_needed = people * slices_per_person / slices_per_pizza
     result = pizzas_needed
     return result

print(solution())