def solution():
    films_with_holy_grail = 5
    holy_grail_movies = ["Excalibur", "Monty Python and the Holy Grail", "Indiana Jones and the Last Crusade",
                         "Prince Killian and the Holy Grail", "The Silver Chalice"]
    if len(holy_grail_movies) >= films_with_holy_grail:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())