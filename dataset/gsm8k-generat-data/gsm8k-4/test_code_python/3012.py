def solution():
    """Amber is baking cakes for her party. She has invited 8 friends and each one will want two slices of cake. Each cake makes 6 slices. If she bakes 4 cakes, how many slices will be left over at the end if she eats three herself?"""
    # Define the number of guests and slices per cake
    guests = 8
    slices_per_guest = 2
    slices_per_cake = 6

    # Calculate the total number of slices needed
    total_slices_needed = guests * slices_per_guest

    # Calculate the total number of slices from the cakes
    total_slices_from_cakes = slices_per_cake * 4

    # Subtract the slices Amber ate and calculate the slices left over
    slices_left_over = total_slices_from_cakes - (total_slices_needed - 3)

    # return the result
    result = slices_left_over
    return result

print(solution())