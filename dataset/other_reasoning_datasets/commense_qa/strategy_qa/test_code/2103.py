def solution():
    french_cuisine = "La Grenouille"
    mexican_cuisine = "salsa"
    if mexican_cuisine not in french_cuisine:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())