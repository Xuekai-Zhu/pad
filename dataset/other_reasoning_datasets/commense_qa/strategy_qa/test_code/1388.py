def solution():
    # Define Sugar Ray Robinson's number of hands and his occupation
    num_hands = 2
    occupation = "boxer"
    # Check if he could still box if he had his hand cut off
    if num_hands >= 1 and occupation != "thief":
        result = "yes"
    else:
        result = "no"
    return result

print(solution())