def solution():
    
    num_people = 6 
    num_pizzas = 3
    num_slices = num_pizzas * 8
    slices_per_person = num_slices / num_people
    result = slices_per_person
    return result

print(solution())