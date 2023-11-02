def solution():
    """Max can trade 3 coconuts for a crab and 6 crabs for a goat. If he has 342 coconuts and he wants to convert all of them into goats, how many goats will he have?"""
    coconuts_per_crab = 3
    crabs_per_goat = 6
    coconuts = 342
    crabs = coconuts // coconuts_per_crab
    goats = crabs // crabs_per_goat
    result = goats
    return result

print(solution())