def solution():
    """A frog lays 800 eggs a year. 10 percent dry up, and 70 percent are eaten. 1/4 of the remaining eggs end up hatching, how many frogs hatch out of the 800?"""
    total_eggs = 800
    dry_up_percentage = 0.10
    eaten_percentage = 0.70
    remaining_eggs = total_eggs - (total_eggs * dry_up_percentage) - (total_eggs * eaten_percentage)
    hatching_percentage = 0.25
    hatched_frogs = remaining_eggs * hatching_percentage
    result = hatched_frogs
    return result

print(solution())