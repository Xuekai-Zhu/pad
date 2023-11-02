def solution():
    characters = ["talking teacup", "sassy duster"]
    inanimate_objects = True
    if inanimate_objects in characters:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())