def solution():
    """Blanch has 15 slices of pizza in the fridge. During breakfast, she eats 4 slices. At lunch, Blanch eats 2 slices, then takes two slices as a snack. Finally, she consumes 5 slices for dinner. How many slices of pizza are left?"""
    # Define the initial number of slices of pizza
    slices_of_pizza = 15

    # Subtract the slices eaten at breakfast
    slices_of_pizza -= 4

    # Subtract the slices eaten at lunch and as a snack
    slices_of_pizza -= 2 + 2

    # Subtract the slices eaten at dinner
    slices_of_pizza -= 5

    # return the result
    result = slices_of_pizza
    return result

print(solution())