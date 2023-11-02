def solution():
    # Calculate the number of omelets to be made for each category of ticket
    small_children_omelets = 0.5 * 53
    older_children_omelets = 35
    adult_omelets = 2 * 75
    senior_omelets = 1.5 * 37

    # Calculate the total number of omelets to be made and add 25 extra omelets
    total_omelets = small_children_omelets + older_children_omelets + adult_omelets + senior_omelets + 25

    # Calculate the number of eggs needed to make all the omelets
    eggs_needed = 2 * total_omelets
    result = eggs_needed
    return result

print(solution())