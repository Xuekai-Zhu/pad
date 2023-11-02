def solution():
    coconuts_per_tree = 5
    coconut_price = 3
    target_income = 90

    # Calculate the total number of coconuts Alvin needs to sell
    total_coconuts_needed = target_income / coconut_price

    # Calculate the number of trees needed to yield the necessary number of coconuts
    num_trees_needed = total_coconuts_needed / coconuts_per_tree
    result = num_trees_needed
    return result

print(solution())