def solution():
    # Define the weight of polecats, sables, and ferrets
    polecat_weight = 2.75
    sable_weight = 2.4
    ferret_weight = 44
    # Check if sables are a good choice to weigh down a scale
    if sable_weight < polecat_weight and sable_weight < ferret_weight:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())