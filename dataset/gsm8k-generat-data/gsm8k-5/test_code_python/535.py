def solution():
    eggs_per_dozen = 12  # There are 12 eggs in a dozen
    dozens_of_eggs = 3  # Tim buys 3 dozen eggs
    cost_per_egg = 0.5  # Eggs cost $0.50 each

    # Calculate the total cost of the eggs
    total_cost = dozens_of_eggs * eggs_per_dozen * cost_per_egg
    result = total_cost
    return result

print(solution())