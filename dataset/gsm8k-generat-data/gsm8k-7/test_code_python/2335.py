def solution():
    slices_per_loaf = 15
    num_friends = 10
    num_loaves = 4

    # Calculate the total number of slices of bread
    total_slices = slices_per_loaf * num_loaves

    # Calculate the number of slices each friend ate
    slices_per_friend = total_slices / num_friends
    result = slices_per_friend
    return result

print(solution())