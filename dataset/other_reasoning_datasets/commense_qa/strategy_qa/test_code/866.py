def solution():
    blooming_onion_possible = False
    onion_size = "large"
    shallot_size = "small"
    if onion_size == "large" and shallot_size == "small":
        blooming_onion_possible = True
    if blooming_onion_possible:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())