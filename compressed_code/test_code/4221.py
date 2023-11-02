def solution():
    
    num_people = 18
    num_slices_per_person = 3
    num_slices_per_pizza = 9
    total_slices_needed = num_people * num_slices_per_person
    num_pizzas_needed = -(-total_slices_needed // num_slices_per_pizza) 
    result = num_pizzas_needed
    return result

print(solution())