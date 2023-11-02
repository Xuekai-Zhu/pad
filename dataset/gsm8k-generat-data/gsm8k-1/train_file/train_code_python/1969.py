def solution():
    """A family bought 1 box of pizza that is cut into 16 slices. Only three-fourths of the pizza was eaten by the family. How many slices of pizza were left?"""
    total_slices = 16
    slices_eaten = total_slices * 0.75
    slices_left = total_slices - slices_eaten
    result = slices_left
    return result

print(solution())