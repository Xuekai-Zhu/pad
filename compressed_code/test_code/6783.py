def solution():
    
    red_straws = 20
    orange_straws = 30
    green_straws = orange_straws / 2
    straws_per_mat = red_straws + orange_straws + green_straws
    mats_to_make = 10
    total_straws_needed = straws_per_mat * mats_to_make
    result = total_straws_needed
    return result

print(solution())