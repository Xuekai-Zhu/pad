def solution():
    num_friends = 4

    pepperoni_slices = 15  # 16 slices - 1 slice left
    cheese_slices = 56  # 16 slices each - 7 slices left

    total_slices = pepperoni_slices + cheese_slices

    # Calculate the number of slices each person eats
    slices_per_person = total_slices / (num_friends - 1)

    result = slices_per_person
    return result

print(solution())