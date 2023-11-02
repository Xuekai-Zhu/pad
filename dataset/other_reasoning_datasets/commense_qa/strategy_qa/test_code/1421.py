def solution():
    is_Janet_follows_Islamic_practice = True
    does_Islamic_culture_avoid_pork = True
    ham_is_made_from_pork = True
    if is_Janet_follows_Islamic_practice and does_Islamic_culture_avoid_pork and ham_is_made_from_pork:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())