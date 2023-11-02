def solution():
    # Calculate the number of Rhode Island Reds in Britney's flock
    britney_RIR = 2 * 11  # Britney has twice as many Rhode Island Reds as Susie

    # Calculate the number of Golden Comets in Britney's flock
    britney_GC = 6 / 2  # Britney has half as many Golden Comets as Susie

    # Calculate the total number of chickens in Britney's flock
    britney_total = britney_RIR + britney_GC

    # Calculate the total number of chickens in Susie's flock
    susie_total = 11 + 6  # Susie has 11 Rhode Island Reds and 6 Golden Comets

    # Calculate the difference in the number of chickens between the two flocks
    difference = britney_total - susie_total
    result = difference
    return result

print(solution())