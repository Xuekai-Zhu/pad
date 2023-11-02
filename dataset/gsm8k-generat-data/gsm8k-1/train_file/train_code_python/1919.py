def solution():
    """Blanch has 15 slices of pizza in the fridge. During breakfast, she eats 4 slices. At lunch, Blanch eats 2 slices, then takes two slices as a snack. Finally, she consumes 5 slices for dinner. How many slices of pizza are left?"""
    slices_in_fridge = 15
    slices_eaten = 4 + 2 + 2 + 5
    slices_left = slices_in_fridge - slices_eaten
    result = slices_left
    return result

print(solution())