def solution():
    # Calculate the total number of straws needed to make 10 mats
    red_straws_per_mat = 20
    orange_straws_per_mat = 30
    green_straws_per_mat = 0.5 * orange_straws_per_mat
    total_straws_per_mat = red_straws_per_mat + orange_straws_per_mat + green_straws_per_mat
    total_straws = total_straws_per_mat * 10
    result = total_straws
    return result

print(solution())