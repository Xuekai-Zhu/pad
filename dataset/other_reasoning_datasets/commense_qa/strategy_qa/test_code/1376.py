def solution():
    movie_location = "Scottish highlands"
    character_country = "Scotland"
    if "Scottish" in movie_location and "Scotland" in character_country:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())