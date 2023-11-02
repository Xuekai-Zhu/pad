def solution():
    movie_title = "Big Daddy"
    main_actors = ["Adam Sandler", "Cole Sprouse"]
    prop_name = "Scuba Steve"
    if main_actors[1] == "Cole Sprouse" and prop_name in movie_title:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())