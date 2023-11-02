def solution():
    # Calculate the number of red stripes on the first flag
    first_flag_red_stripes = 1

    # Calculate the number of total stripes on one flag
    total_stripes = 13

    # Calculate the number of non-red stripes on one flag
    non_red_stripes = total_stripes - first_flag_red_stripes

    # Calculate the number of red stripes on the remaining flags
    remaining_flags_red_stripes = (non_red_stripes / 2) * (10 - 1)

    # Calculate the total number of red stripes
    total_red_stripes = first_flag_red_stripes + remaining_flags_red_stripes
    result = total_red_stripes
    return result

print(solution())