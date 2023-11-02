def solution():
    necessary_conditions = ["water", "oxygen", "light"]
    sesame_seed_conditions = ["not in the human body"]
    overlap = [condition for condition in necessary_conditions if condition in sesame_seed_conditions]
    if overlap:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())