def solution():
    """A frog lays 800 eggs a year. 10 percent dry up, and 70 percent are eaten. 1/4 of the remaining eggs end up hatching, how many frogs hatch out of the 800?"""
    # Calculate the number of eggs that dry up
    dry_up = 0.1 * 800

    # Calculate the number of eggs that are eaten
    eaten = 0.7 * 800

    # Calculate the number of eggs that remain
    remaining = 800 - dry_up - eaten

    # Calculate the number of eggs that end up hatching
    hatching = 0.25 * remaining

    # Display the number of frogs that hatch out of the 800 eggs
    result = hatching
    return result

print(solution())