def solution():
    """A frog lays 800 eggs a year. 10 percent dry up, and 70 percent are eaten. 1/4 of the remaining eggs end up hatching, how many frogs hatch out of the 800?"""
    # Define the initial number of eggs
    num_eggs = 800

    # Calculate the percentage of eggs that dry up
    dry_up_percent = 10

    # Calculate the number of eggs that dry up
    dry_up_eggs = num_eggs * (dry_up_percent / 100)

    # Calculate the percentage of eggs that are eaten
    eaten_percent = 70

    # Calculate the number of eggs that are eaten
    eaten_eggs = num_eggs * (eaten_percent / 100)

    # Calculate the number of eggs that remain
    remaining_eggs = num_eggs - dry_up_eggs - eaten_eggs

    # Calculate the percentage of remaining eggs that hatch
    hatch_percent = 25

    # Calculate the number of eggs that hatch
    hatch_eggs = remaining_eggs * (hatch_percent / 100)

    # Return the number of hatched frogs
    result = hatch_eggs
    return result

print(solution())