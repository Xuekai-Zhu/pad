def solution():
    preschoolers_age_min = 3
    preschoolers_age_max = 5
    movie_rating = "PG-13"
    if preschoolers_age_max < int(movie_rating[3:]):
        result = "no"
    else:
        result = "yes"
    return result

print(solution())