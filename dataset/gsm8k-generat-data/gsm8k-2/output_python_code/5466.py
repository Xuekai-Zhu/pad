def solution():
    """There is a group of 18 people who are ordering pizza. If each person gets 3 slices and each pizza has 9 slices, how many pizzas should they order?"""
    num_people = 18
    num_slices_per_person = 3
    num_slices_per_pizza = 9
    total_slices_needed = num_people * num_slices_per_person
    num_pizzas_needed = -(-total_slices_needed // num_slices_per_pizza) # Round up division
    result = num_pizzas_needed
    return result

print(solution())