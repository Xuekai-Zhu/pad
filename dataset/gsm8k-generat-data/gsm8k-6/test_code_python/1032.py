def solution():
    # Calculate the number of chickens in Susie's flock
    susie_RIR = 11  # Rhode Island Reds in Susie's flock
    susie_GC = 6  # Golden Comets in Susie's flock

    # Calculate the number of chickens in Britney's flock
    britney_RIR = 2 * susie_RIR  # twice as many Rhode Island Reds as Susie
    britney_GC = susie_GC / 2  # half as many Golden Comets as Susie

    # Calculate the difference in the number of chickens in the two flocks
    diff_chickens = (britney_RIR + britney_GC) - (susie_RIR + susie_GC)

    result = diff_chickens
    return result

print(solution())