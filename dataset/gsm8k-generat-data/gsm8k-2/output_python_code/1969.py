def solution():
    """A family bought 1 box of pizza that is cut into 16 slices. Only three-fourths of the pizza was eaten by the family. How many slices of pizza were left?"""
    total_slices = 16
    eaten_slices = int(total_slices * 0.75)
    leftover_slices = total_slices - eaten_slices
    result = leftover_slices
    return result

print(solution())