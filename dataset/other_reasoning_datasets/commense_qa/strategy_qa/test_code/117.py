def solution():
    movie_title = "The Fly"
    insect_used_in_movie = "Housefly"
    closely_related_insects = ["Black fly", "Chironomidae"]
    if "Black fly" not in closely_related_insects:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())