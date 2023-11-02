def solution():
    num_stars = 5
    lowest_desired_star_rating = 2
    if num_stars >= lowest_desired_star_rating:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())