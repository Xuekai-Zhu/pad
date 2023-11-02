def solution():
    """A family had 10 eggs, but the mother used 5 of them to make an omelet. Then, 2 chickens laid 3 eggs each. How many eggs does the family have now?"""
    initial_eggs = 10
    used_eggs = 5
    eggs_laid = 2 * 3
    total_eggs = initial_eggs - used_eggs + eggs_laid
    result = total_eggs
    return result

print(solution())