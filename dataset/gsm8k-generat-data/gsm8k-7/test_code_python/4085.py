def solution():
    first_anthill = 100
    reduction = 0.2

    # Calculate the number of ants in the second anthill
    second_anthill = first_anthill * (1 - reduction)

    # Calculate the number of ants in the third anthill
    third_anthill = second_anthill * (1 - reduction)

    result = third_anthill
    return result

print(solution())