def solution():
    num_stripes = 13
    num_flags = 10

    # Calculate the number of red stripes on the first flag
    num_red_stripes_first_flag = 1

    # Calculate the total number of remaining stripes
    num_remaining_stripes = num_stripes - 1

    # Calculate the number of red stripes on each remaining flag
    num_red_stripes_remaining_flags = num_remaining_stripes / 2

    # Calculate the total number of red stripes on all flags
    total_red_stripes = (num_red_stripes_first_flag + num_red_stripes_remaining_flags) * num_flags
    result = total_red_stripes
    return result

print(solution())