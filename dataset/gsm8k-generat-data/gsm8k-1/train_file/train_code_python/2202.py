def solution():
    """Ben has 20 eggs in the fridge. Yesterday, he ate 4 eggs in the morning and 3 in the afternoon. How many eggs does Ben have now?"""
    initial_eggs = 20
    morning_eggs = 4
    afternoon_eggs = 3
    remaining_eggs = initial_eggs - morning_eggs - afternoon_eggs
    result = remaining_eggs
    return result

print(solution())