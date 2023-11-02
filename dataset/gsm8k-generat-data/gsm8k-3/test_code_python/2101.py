def solution():
    """Brenda and nine of her friends want to order a pizza. They decide that each person will eat 2 slices. If each pizza has 4 slices, how many pizzas should they order?"""
    # Define the number of people and slices per person
    num_people = 10
    slices_per_person = 2

    # Calculate the total number of slices needed
    total_slices = num_people * slices_per_person

    # Calculate the number of pizzas needed
    pizzas_needed = total_slices / 4

    # Round up to the nearest integer (since you can't order a fractional pizza)
    pizzas_needed = math.ceil(pizzas_needed)

    # Display the number of pizzas needed
    result = pizzas_needed
    return result

print(solution())