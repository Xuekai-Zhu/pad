def solution():
    # Calculate the number of eggs that dry up
    dry_eggs = 0.1 * 800

    # Calculate the number of eggs that are eaten
    eaten_eggs = 0.7 * 800

    # Calculate the number of remaining eggs
    remaining_eggs = 800 - dry_eggs - eaten_eggs

    # Calculate the number of eggs that end up hatching
    hatching_eggs = 0.25 * remaining_eggs

    result = hatching_eggs
    return result

print(solution())