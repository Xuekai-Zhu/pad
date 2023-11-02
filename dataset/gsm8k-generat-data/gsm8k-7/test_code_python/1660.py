def solution():
    num_green_papayas = 14
    num_yellow_friday = 2
    num_yellow_sunday = 2 * num_yellow_friday

    # Calculate the total number of papayas that turned yellow
    total_yellow = num_yellow_friday + num_yellow_sunday

    # Calculate the number of green papayas left on the tree
    num_green_left = num_green_papayas - total_yellow
    result = num_green_left
    return result

print(solution())