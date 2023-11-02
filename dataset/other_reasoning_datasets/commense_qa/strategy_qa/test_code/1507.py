def solution():
    members_of_the_police_are_musicians = True
    only_law_enforcement_can_arrest = True
    if members_of_the_police_are_musicians and only_law_enforcement_can_arrest:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())