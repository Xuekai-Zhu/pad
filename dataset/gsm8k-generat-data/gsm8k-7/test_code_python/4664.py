def solution():
    num_slices = 1  # initially one unsliced pizza
    num_cuts = 3  # number of cuts made by Phill
    num_friends_with_1_slice = 3
    num_friends_with_2_slices = 2

    # Each cut doubles the number of slices
    for i in range(num_cuts):
        num_slices *= 2

    # Subtract the slices given to friends
    num_slices -= (num_friends_with_1_slice * 1) + (num_friends_with_2_slices * 2)

    result = num_slices
    return result

print(solution())