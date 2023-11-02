def solution():
    disney_second_film_year = 1940
    jonah_story = "swallowed by a whale"
    gepetto_story = "swallowed by a giant whale"
    if jonah_story in gepetto_story and disney_second_film_year > 700:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())