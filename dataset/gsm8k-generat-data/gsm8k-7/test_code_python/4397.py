def solution():
    coconuts = 342
    crab_per_coconut = 1/3
    goats_per_crab = 1/6

    # Calculate the number of crabs Max can get for all his coconuts
    crabs = coconuts * crab_per_coconut

    # Calculate the number of goats Max can get for all his crabs
    goats = crabs * goats_per_crab

    result = goats
    return result

print(solution())