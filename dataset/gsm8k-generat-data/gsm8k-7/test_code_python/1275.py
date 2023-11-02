def solution():
    num_mats = 10
    red_straws_per_mat = 20
    orange_straws_per_mat = 30
    green_straws_per_mat = orange_straws_per_mat / 2

    # Calculate the total number of red straws needed for all mats
    total_red_straws = num_mats * red_straws_per_mat

    # Calculate the total number of orange straws needed for all mats
    total_orange_straws = num_mats * orange_straws_per_mat

    # Calculate the total number of green straws needed for all mats
    total_green_straws = num_mats * green_straws_per_mat

    # Calculate the total number of straws needed for all mats
    total_straws = total_red_straws + total_orange_straws + total_green_straws
    result = total_straws
    return result

print(solution())