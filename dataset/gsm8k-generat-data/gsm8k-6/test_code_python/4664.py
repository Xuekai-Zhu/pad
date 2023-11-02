def solution():
    # Calculate the number of slices of pizza Phill has after cutting
    num_slices = 1 + 2 + 4 + 8  # He cuts the pizza into halves, then quarters, then eighths, so there are a total of 15 slices
    num_friends_with_1_slice = 3
    num_friends_with_2_slices = 2

    # Calculate the number of slices of pizza Phill gives to his friends
    num_slices_given_away = num_friends_with_1_slice * 1 + num_friends_with_2_slices * 2

    # Calculate the number of slices of pizza Phill has left
    num_slices_left = num_slices - num_slices_given_away
    result = num_slices_left
    return result

print(solution())