def solution():
    mnm_to_star_ratio = 5 / 3
    num_mnms = 25

    # Calculate the total number of Starburst candies using the ratio and the number of M&Ms
    total_starbursts = (num_mnms / mnm_to_star_ratio) * 3

    result = total_starbursts
    return result

print(solution())