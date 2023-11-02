def solution():
    popular_disney_characters = ["Mickey Mouse", "Donald Duck", "Olaf", "Elsa"]
    made_of_living_ice = ["Olaf"]
    overlap = [character for character in popular_disney_characters if character in made_of_living_ice]
    if overlap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())