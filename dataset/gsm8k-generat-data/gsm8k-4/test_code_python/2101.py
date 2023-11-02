def solution():
    """Brenda and nine of her friends want to order a pizza. They decide that each person will eat 2 slices. If each pizza has 4 slices, how many pizzas should they order?"""
    # Define the number of people and slices per person
    num_people = 10
    slices_per_person = 2

    # Calculate the total number of slices needed
    total_slices = num_people * slices_per_person

    # Calculate the number of pizzas needed
    slices_per_pizza = 4
    pizzas_needed = total_slices / slices_per_pizza

    # Round up to the nearest integer
    pizzas_needed = int(pizzas_needed + 0.9)

    # Return the result
    result = pizzas_needed
    return result

print(solution())