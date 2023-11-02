def solution():
    """A loaf of bread was sliced into 15. Ten friends bought 4 loaves of bread.
    If they all eat all 4 loaves equally, how many slices of bread did each of them eat?"""
    # Define the number of slices per loaf
    slices_per_loaf = 15

    # Calculate the total number of slices
    total_slices = slices_per_loaf * 4

    # Calculate the number of slices each friend will eat if they split the bread equally
    slices_per_friend = total_slices / 10

    # Return the result
    result = slices_per_friend
    return result

print(solution())