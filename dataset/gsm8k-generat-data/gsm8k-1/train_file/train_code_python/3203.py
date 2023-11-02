def solution():
    """Mark has two dozen eggs to split with his three siblings. How many eggs does each person get to eat if they all eat the same amount?"""
    eggs_per_dozen = 12
    total_eggs = 2 * eggs_per_dozen
    siblings = 3
    eggs_per_person = total_eggs / siblings
    result = eggs_per_person
    return result

print(solution())