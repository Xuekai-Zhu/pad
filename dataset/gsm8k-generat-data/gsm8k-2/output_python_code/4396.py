def solution():
    """Max can trade 3 coconuts for a crab and 6 crabs for a goat. If he has 342 coconuts and he wants to convert all of them into goats, how many goats will he have?"""
    coconuts = 342
    crabs = coconuts // 3
    goats = crabs // 6
    result = goats
    return result

print(solution())