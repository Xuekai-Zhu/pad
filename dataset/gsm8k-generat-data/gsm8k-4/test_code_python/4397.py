def solution():
    """Max can trade 3 coconuts for a crab and 6 crabs for a goat. If he has 342 coconuts and he wants to convert all of them into goats, how many goats will he have?"""
    # Define the conversion rates
    CRAB_PER_3_COCONUTS = 1
    GOAT_PER_6_CRABS = 1

    # Calculate the number of crabs Max can get for his coconuts
    total_crabs = (342 // 3) * CRAB_PER_3_COCONUTS

    # Calculate the number of goats Max can get for his crabs
    total_goats = (total_crabs // 6) * GOAT_PER_6_CRABS

    # Return the number of goats
    result = total_goats
    return result

print(solution())