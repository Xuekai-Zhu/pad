def solution():
    saltwater_crocodile_family = "Crocodylinae"
    alligator_family = "Alligatoridae"
    if saltwater_crocodile_family in alligator_family:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())