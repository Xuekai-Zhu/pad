def solution():
    """John with his five friends ordered 3 pizzas. Each pizza had 8 slices. If they all finished and ate the same amount of pizzas, how many slices did each person eat?"""
    # Define the number of pizzas and slices per pizza
    PIZZA_COUNT = 3
    SLICES_PER_PIZZA = 8

    # Define the number of people sharing the pizzas
    PEOPLE_COUNT = 6  # John and his five friends

    # Calculate the total number of slices
    total_slices = PIZZA_COUNT * SLICES_PER_PIZZA

    # Calculate the number of slices per person
    slices_per_person = total_slices / PEOPLE_COUNT

    # Display the number of slices per person
    result = slices_per_person
    return result

print(solution())