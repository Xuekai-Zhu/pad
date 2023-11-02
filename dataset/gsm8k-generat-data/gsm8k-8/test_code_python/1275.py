def solution():
    # Define the amount of each color straw needed for one mat
    red_straws_per_mat = 20
    orange_straws_per_mat = 30
    green_straws_per_mat = 0.5 * orange_straws_per_mat

    # Calculate the total number of straws needed for 10 mats
    total_red_straws = 10 * red_straws_per_mat
    total_orange_straws = 10 * orange_straws_per_mat
    total_green_straws = 10 * green_straws_per_mat

    total_straws = total_red_straws + total_orange_straws + total_green_straws
    result = total_straws
    return result

print(solution())