def solution():
    
    num_people = 6  
    num_pizzas = 3
    slices_per_pizza = 8
    total_slices = num_pizzas * slices_per_pizza
    slices_per_person = total_slices / num_people
    result = slices_per_person
    return result

print(solution())