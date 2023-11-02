def solution():
    racist_characters = ["Baloo", "snake character", "King Louie"]
    racist_descriptions = ["mocking a common black feature", "made to sound like an Indian mag", "viewed socially as a racist archetype of a black man"]
    if any(racist_characters) and any(racist_descriptions):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())