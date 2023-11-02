def solution():
    """Mark has two dozen eggs to split with his three siblings. How many eggs does each person get to eat if they all eat the same amount?"""
    total_eggs = 2 * 12  # converting dozen to individual eggs
    total_people = 4  # Mark and his 3 siblings
    eggs_per_person = total_eggs / total_people
    result = eggs_per_person
    return result

print(solution())