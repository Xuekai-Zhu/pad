def solution():
    
    red_straws_per_mat = 20
    orange_straws_per_mat = 30
    green_straws_per_mat = 0.5 * orange_straws_per_mat
    total_straws_per_mat = red_straws_per_mat + orange_straws_per_mat + green_straws_per_mat
    mats_to_weave = 10
    total_straws_needed = total_straws_per_mat * mats_to_weave
    result = total_straws_needed
    return result

print(solution())