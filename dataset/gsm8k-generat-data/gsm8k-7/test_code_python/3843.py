def solution():
    num_slices = 8
    joe_share = 1/2
    darcy_share = 1/2
    carl_share = 1/4

    # Calculate the total number of slices given away
    total_given_away = joe_share + darcy_share + carl_share

    # Calculate the number of slices left
    slices_left = num_slices - total_given_away*num_slices
    result = slices_left
    return result

print(solution())