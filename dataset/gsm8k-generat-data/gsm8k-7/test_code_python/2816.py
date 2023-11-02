def solution():
    num_eggs = 800

    # Calculate the number of eggs that dry up
    dry_up = num_eggs * 0.1

    # Calculate the number of eggs that are eaten
    eaten = num_eggs * 0.7

    # Calculate the number of eggs that remain
    remaining = num_eggs - dry_up - eaten

    # Calculate the number of eggs that end up hatching
    hatch = remaining / 4

    result = hatch
    return result

print(solution())