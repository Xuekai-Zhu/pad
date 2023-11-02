def solution():
    crocodile_habitat = "salt water"
    alligator_habitat = "fresh water"
    can_crocodiles_breathe_underwater = True
    can_alligators_breathe_underwater = False
    if crocodile_habitat == "salt water" and can_crocodiles_breathe_underwater:
        crocodile_survival = "longer"
    else:
        crocodile_survival = "not applicable"
    if alligator_habitat == "salt water" and can_alligators_breathe_underwater:
        alligator_survival = "longer"
    else:
        alligator_survival = "not applicable"
    if crocodile_survival == "longer" and alligator_survival == "not applicable":
        result = "yes"
    else:
        result = "no"
    return result

print(solution())