def solution():
    """A family had 10 eggs, but the mother used 5 of them to make an omelet. Then, 2 chickens laid 3 eggs each. How many eggs does the family have now?"""
    starting_eggs = 10
    used_eggs = 5
    remaining_eggs = starting_eggs - used_eggs
    chicken_laid_eggs = 2 * 3
    total_eggs = remaining_eggs + chicken_laid_eggs
    result = total_eggs
    return result

print(solution())