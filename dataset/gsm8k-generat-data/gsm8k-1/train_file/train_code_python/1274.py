def solution():
    """Ginger is weaving mats out of colored straw. Each mat takes 20 red straws, 30 orange straws, and half as many green straws as orange straws. How many straws does she need to make 10 mats?"""
    red_straws = 20
    orange_straws = 30
    green_straws = orange_straws / 2
    straws_per_mat = red_straws + orange_straws + green_straws
    mats_to_make = 10
    total_straws_needed = straws_per_mat * mats_to_make
    result = total_straws_needed
    return result

print(solution())