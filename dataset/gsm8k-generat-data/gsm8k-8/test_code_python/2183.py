def solution():
    #Calculate the total number of planks used without accounting for the ruined ones and the leftovers
    total_planks_used = 8 + 20 + 11 + (8 - 2) + (2 * 4) + (2 * 3 * 2)

    #Account for the ruined planks
    total_planks_used += 2 * 3

    #Add the leftover planks
    total_planks_used += 6

    result = total_planks_used
    return result

print(solution())