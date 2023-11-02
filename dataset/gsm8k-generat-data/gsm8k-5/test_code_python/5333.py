def solution():
    bell_pepper_slices = 5 * 20  # Tamia cuts each of the 5 bell peppers into 20 slices
    small_bell_pepper_pieces = (bell_pepper_slices / 2) * 3  # Tamia takes half of the slices and cuts them into 3 smaller pieces each

    # Calculate the total number of slices and pieces of bell pepper Tamia will add to the meal
    total_bell_pepper_pieces = bell_pepper_slices + small_bell_pepper_pieces
    result = total_bell_pepper_pieces
    return result

print(solution())