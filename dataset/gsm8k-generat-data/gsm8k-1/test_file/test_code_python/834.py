def solution():
    """Adam wants to eat some sliced apples. A large apple can be sliced into 5 pieces, and a small apple can be sliced into 3 pieces. Adam decides to slice 3 large and 5 small apples and then eats 15 slices. How many apple slices are left?"""
    large_slices = 5
    small_slices = 3
    large_apples = 3
    small_apples = 5
    total_slices = (large_slices * large_apples) + (small_slices * small_apples)
    slices_eaten = 15
    slices_left = total_slices - slices_eaten
    result = slices_left
    return result

print(solution())