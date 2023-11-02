def solution():
    slices_per_pizza = 18
    pizzas_ordered = 6
    cheese_leftover = 8
    onion_leftover = 4
    cheese_per_student = 2
    onion_per_student = 1
 
    total_cheese = cheese_per_student * slices_per_pizza * pizzas_ordered + cheese_leftover
    total_onion = onion_per_student * slices_per_pizza * pizzas_ordered + onion_leftover
 
    num_students = (total_cheese / cheese_per_student) / (slices_per_pizza / cheese_per_student)
 
    result = num_students
    return result

print(solution())