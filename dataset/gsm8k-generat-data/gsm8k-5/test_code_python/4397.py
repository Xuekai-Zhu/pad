def solution():
    # Calculate the number of crabs Max can get for 342 coconuts
    crabs = (342 // 3)

    # Calculate the number of goats Max can get for the crabs
    goats = crabs // 6

    result = goats
    return result

print(solution())