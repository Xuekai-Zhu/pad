def solution():
    # Calculate the total number of coconuts needed to make $90
    total_coconuts_needed = 90 / 3

    # Calculate the number of trees required to yield the required number of coconuts
    trees_needed = total_coconuts_needed / 5
    result = trees_needed
    return result

print(solution())