def solution():
    bee_exoskeleton = "chitin"
    human_stomach_abilities = ["release harsh acids", "break down glucose in 33 hours"]
    if bee_exoskeleton in human_stomach_abilities:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())