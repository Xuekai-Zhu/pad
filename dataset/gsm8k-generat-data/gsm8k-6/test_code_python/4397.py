def solution():
    # Calculate the number of crabs Max can get with 342 coconuts
    num_crabs = (342//3)  # 3 coconuts for a crab
    # Calculate the number of goats Max can get with the crabs he has
    num_goats = num_crabs // 6  # 6 crabs for a goat
    result = num_goats
    return result

print(solution())