def solution():
    """James and Lisa ordered 2 small pizzas. Each pizza has 6 slices. James ate 2/3 of all the slices. How many slices of pizza did James eat?"""
    # Define the number of pizzas and slices per pizza
    PIZZA_COUNT = 2
    SLICES_PER_PIZZA = 6

    # Calculate the total number of slices
    total_slices = PIZZA_COUNT * SLICES_PER_PIZZA

    # Calculate the number of slices James ate
    james_slices = total_slices * (2/3)

    # Display the number of slices James ate
    result = james_slices
    return result

print(solution())