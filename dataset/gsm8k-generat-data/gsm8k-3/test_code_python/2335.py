def solution():
    """A loaf of bread was sliced into 15. Ten friends bought 4 loaves of bread. If they all eat all 4 loaves equally, how many slices of bread did each of them eat?"""
    # Define the number of slices per loaf of bread
    SLICES_PER_LOAF = 15

    # Define the number of loaves of bread bought
    num_loaves = 4

    # Calculate the total number of slices of bread
    total_slices = num_loaves * SLICES_PER_LOAF

    # Calculate the number of slices each friend ate
    num_friends = 10
    slices_per_friend = total_slices / num_friends

    # Display the number of slices each friend ate
    result = slices_per_friend
    return result

print(solution())