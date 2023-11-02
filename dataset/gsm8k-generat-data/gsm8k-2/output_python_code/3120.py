def solution():
    """A whole pizza was cut into 8 slices. Angeli and Marlon ate 3/2 slices each. How many slices of pizza are left?"""
    pizza_slices = 8
    angeli_slices = 3/2
    marlon_slices = 3/2
    total_slices_eaten = angeli_slices + marlon_slices
    slices_left = pizza_slices - total_slices_eaten
    result = slices_left
    return result

print(solution())