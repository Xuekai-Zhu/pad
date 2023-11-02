def solution():
    birth_name = "Gaius Octavius"
    adopted_name = "Gaius Iulius Caesar"
    emperor_name = "Augustus"
    if emperor_name != birth_name and emperor_name != adopted_name:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())