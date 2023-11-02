def solution():
    # Calculate the number of eggs that dry up
    dry_up = 0.1 * 800

    # Calculate the number of eggs that are eaten
    eaten = 0.7 * 800

    # Calculate the number of remaining eggs
    remaining_eggs = 800 - dry_up - eaten

    # Calculate the number of eggs that hatch
    hatch = 0.25 * remaining_eggs

    result = hatch
    return result

print(solution())