def solution():
    """Ben has two brothers. They can each eat 12 slices of pizza. They are ordering pizza for the night and want to make sure they get enough. The large pizzas have 14 slices and the small pizzas have 8. If they order 1 small pizza, how many large pizzas do they need to order?"""
    # Define the number of slices each person can eat
    SLICES_PER_PERSON = 12

    # Define the number of slices per large and small pizza
    LARGE_SLICES = 14
    SMALL_SLICES = 8

    # Define the number of people eating pizza
    num_people = 3

    # Calculate the number of slices needed
    slices_needed = num_people * SLICES_PER_PERSON - SMALL_SLICES

    # Calculate the number of large pizzas needed
    num_large_pizzas = slices_needed // LARGE_SLICES + (slices_needed % LARGE_SLICES > 0)

    # Display the number of large pizzas needed
    result = num_large_pizzas
    return result

print(solution())