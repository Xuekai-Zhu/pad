def solution():
    """Max can trade 3 coconuts for a crab and 6 crabs for a goat. If he has 342 coconuts and he wants to convert all of them into goats, how many goats will he have?"""
    # Define the exchange rate of coconuts for crabs and crabs for goats
    COCONUTS_PER_CRAB = 3
    CRABS_PER_GOAT = 6

    # Calculate the number of crabs Max can get with 342 coconuts
    crabs = 342 // COCONUTS_PER_CRAB

    # Calculate the number of goats Max can get with the crabs he has
    goats = crabs // CRABS_PER_GOAT

    # Display the number of goats Max can get with 342 coconuts
    result = goats
    return result

print(solution())