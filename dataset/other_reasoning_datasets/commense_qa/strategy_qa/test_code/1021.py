def solution():
    movie_title = "Jack Frost"
    has_groundhog_character = True
    mentions_groundhog_day = True
    if movie_title and has_groundhog_character and mentions_groundhog_day:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())