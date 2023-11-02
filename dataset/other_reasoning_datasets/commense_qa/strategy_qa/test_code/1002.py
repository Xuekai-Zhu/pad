def solution():
    cause_of_death = "pancreatic cancer"
    improperly_functioning_organ = "pancreas"
    if cause_of_death.startswith(improperly_functioning_organ):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())