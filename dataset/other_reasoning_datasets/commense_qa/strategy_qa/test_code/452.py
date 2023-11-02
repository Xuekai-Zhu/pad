def solution():
    staff_member = "Igor Karkaroff"
    former_death_eater = True
    if former_death_eater:
        voldemorts_minions = ["Death Eaters"]
        if "Durmstrang" in voldemorts_minions and staff_member in voldemorts_minions:
            result = "yes"
        else:
            result = "no"
    else:
        result = "no"
    return result

print(solution())