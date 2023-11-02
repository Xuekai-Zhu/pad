def solution():
    ariel_hair_color = "red"
    disney_princess_on_broadway = True
    if disney_princess_on_broadway:
        princess_hair_color = "red"
        if princess_hair_color == ariel_hair_color:
            result = "yes"
        else:
            result = "no"
    else:
        result = "no"
    return result

print(solution())