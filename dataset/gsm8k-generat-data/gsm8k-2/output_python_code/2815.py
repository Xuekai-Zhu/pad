def solution():
    """A frog lays 800 eggs a year. 10 percent dry up, and 70 percent are eaten. 1/4 of the remaining eggs end up hatching, how many frogs hatch out of the 800?"""
    total_eggs = 800
    dry_eggs = total_eggs * 0.1
    remaining_eggs = total_eggs - dry_eggs
    eaten_eggs = remaining_eggs * 0.7
    hatching_eggs = (remaining_eggs - eaten_eggs) / 4
    result = hatching_eggs
    return result

print(solution())