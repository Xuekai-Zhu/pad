def solution():
    # Calculate the number of crabs Max can get from the coconuts
    num_crabs = 342 // 3
    
    # Calculate the number of goats Max can get from the crabs
    num_goats = num_crabs // 6
    
    result = num_goats
    return result

print(solution())