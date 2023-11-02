def solution():
    apples_sliced = 2
    slices_per_apple = 8
    total_slices = apples_sliced * slices_per_apple
    slices_given = total_slices * 3/8
    slices_eaten = (total_slices - slices_given) / 2
    slices_left = total_slices - slices_given - slices_eaten
    result = slices_left
    return result

print(solution())