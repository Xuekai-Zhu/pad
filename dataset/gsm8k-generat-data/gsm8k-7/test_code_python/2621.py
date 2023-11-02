def solution():
    num_pink_hangers = 7
    num_green_hangers = 4
    num_blue_hangers = num_green_hangers - 1
    num_yellow_hangers = num_blue_hangers - 1

    # Calculate the total number of colored hangers
    total_hangers = num_pink_hangers + num_green_hangers + num_blue_hangers + num_yellow_hangers
    result = total_hangers
    return result

print(solution())