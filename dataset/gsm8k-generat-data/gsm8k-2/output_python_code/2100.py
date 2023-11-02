def solution():
    """Brenda and nine of her friends want to order a pizza. They decide that each person will eat 2 slices. If each pizza has 4 slices, how many pizzas should they order?"""
    num_people = 10
    slices_per_person = 2
    slices_per_pizza = 4
    total_slices_needed = num_people * slices_per_person
    pizzas_needed = total_slices_needed / slices_per_pizza
    result = pizzas_needed
    return result

print(solution())