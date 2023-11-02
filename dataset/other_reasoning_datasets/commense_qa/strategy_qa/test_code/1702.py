def solution():
    is_learning_disability_neurological = True
    penicillin_treats_bacterial_infections = True
    if is_learning_disability_neurological and not penicillin_treats_bacterial_infections:
        result = "no"
    else:
        result = "not applicable"
    return result

print(solution())