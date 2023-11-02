def solution():
    """A whole pizza was cut into 8 slices. Angeli and Marlon ate 3/2 slices each. How many slices of pizza are left?"""
    whole_pizza = 8
    slices_eaten = 3/2
    total_slices_eaten = 2 * slices_eaten
    slices_left = whole_pizza - total_slices_eaten
    result = slices_left
    return result

print(solution())