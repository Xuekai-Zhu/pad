def solution():
    
    num_goats = 4
    num_carrots = 47
    carrots_per_goat = num_carrots // num_goats
    leftovers = num_carrots % num_goats
    result = leftovers
    return result

print(solution())