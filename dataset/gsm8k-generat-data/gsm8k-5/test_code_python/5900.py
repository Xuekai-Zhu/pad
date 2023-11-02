def solution():
    coconuts_per_tree = 5  # Each tree yields 5 coconuts
    price_per_coconut = 3  # Each coconut can be sold for $3
    required_income = 90  # Alvin needs $90

    # Calculate the total number of coconuts Alvin needs to sell
    total_coconuts_needed = required_income / price_per_coconut

    # Calculate the number of trees Alvin needs to harvest based on the number of coconuts
    trees_needed = total_coconuts_needed / coconuts_per_tree
    result = trees_needed
    return result

print(solution())