def solution():
    total_eggs = 800  # A frog lays 800 eggs a year

    # Calculate the number of eggs that dry up and are eaten
    dry_eggs = 0.1 * total_eggs
    eaten_eggs = 0.7 * total_eggs
    remaining_eggs = total_eggs - dry_eggs - eaten_eggs

    # Calculate the number of eggs that end up hatching
    hatching_eggs = 0.25 * remaining_eggs

    result = hatching_eggs
    return result

print(solution())