def solution():
    # Calculate the number of glasses in each cupboard
    tall_cupboard = 20
    wide_cupboard = 2 * tall_cupboard
    narrow_cupboard = 15 * 2  # The narrow cupboard has two shelves
    remaining_narrow_shelf = narrow_cupboard % 2  # Check if there is a broken shelf in the narrow cupboard
    if remaining_narrow_shelf == 1:  # If there is a broken shelf...
        narrow_cupboard -= 15  # ... remove the glasses on that shelf

    # Calculate the total number of glasses displayed
    total_glasses = tall_cupboard + wide_cupboard + narrow_cupboard
    result = total_glasses
    return result

print(solution())