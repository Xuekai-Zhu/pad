def solution():
    # Define the weights in terms of Ben's weight
    ben_weight = 1
    carl_weight = ben_weight + 16
    al_weight = ben_weight + 25
    ed_weight = al_weight - 38

    # Solve for Ben's weight
    ben_weight = ed_weight + 38 - 25

    # Solve for Carl's weight
    carl_weight = ben_weight + 16

    result = carl_weight
    return result

print(solution())