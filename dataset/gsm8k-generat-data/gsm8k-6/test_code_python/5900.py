def solution():
    # Calculate the number of coconuts needed to make $90
    coconuts_needed = 90 / 3  # each coconut can be sold for $3
    # Calculate the number of trees needed to yield the required number of coconuts
    trees_needed = coconuts_needed / 5  # each tree yields 5 coconuts
    result = trees_needed
    return result

print(solution())