def solution():
    """Addilynn went to the grocery store and bought six dozen eggs for use in her house. After two weeks, she used half of the eggs, then accidentally broke 15 of the remaining eggs while moving them to clean the shelves. How many eggs are left on the shelf?"""
    total_eggs = 6 * 12
    used_eggs = total_eggs / 2
    remaining_eggs = total_eggs - used_eggs
    remaining_eggs -= 15
    result = remaining_eggs
    return result

print(solution())