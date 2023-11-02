def solution():
    demi_lovato_mexican_ancestry = True
    maize_domesticated_in_southern_mexico = True
    popcorn_made_from_corn = True
    if demi_lovato_mexican_ancestry and maize_domesticated_in_southern_mexico and popcorn_made_from_corn:
        result = "possibly"
    else:
        result = "no"
    return result

print(solution())