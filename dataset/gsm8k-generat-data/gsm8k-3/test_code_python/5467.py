def solution():
    """There is a group of 18 people who are ordering pizza. If each person gets 3 slices and each pizza has 9 slices, how many pizzas should they order?"""
    # Define the number of people and slices per person
    NUM_PEOPLE = 18
    SLICES_PER_PERSON = 3

    # Calculate the total number of slices needed
    total_slices = NUM_PEOPLE * SLICES_PER_PERSON

    # Calculate the number of pizzas needed, rounding up to the nearest integer
    pizzas_needed = math.ceil(total_slices / 9)

    # Display the number of pizzas needed
    result = pizzas_needed
    return result

print(solution())