def solution():
    red_straws_per_mat = 20
    orange_straws_per_mat = 30
    green_straws_per_mat = orange_straws_per_mat / 2
    mats_to_make = 10

    # Calculate the total number of straws needed to make 10 mats
    total_red_straws = red_straws_per_mat * mats_to_make
    total_orange_straws = orange_straws_per_mat * mats_to_make
    total_green_straws = green_straws_per_mat * mats_to_make
    total_straws = total_red_straws + total_orange_straws + total_green_straws
    result = total_straws
    return result

print(solution())