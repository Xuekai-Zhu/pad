def solution():
    # Calculate the total number of slices in 4 loaves of bread
    total_slices = 15 * 4  # each loaf has 15 slices

    # Calculate the number of slices each friend eats
    num_friends = 10
    slices_per_friend = total_slices / num_friends

    result = slices_per_friend
    return result

print(solution())