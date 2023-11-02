def solution():
    
    coconuts_per_crab = 3
    crabs_per_goat = 6
    coconuts = 342
    crabs = coconuts // coconuts_per_crab
    goats = crabs // crabs_per_goat
    result = goats
    return result

print(solution())