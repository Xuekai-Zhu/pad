def solution():
    """Lyssa and Precious took an English proficiency exam. Lyssa answered 20% of the items incorrectly. Precious got 12 mistakes. How many more correct answers did Lyssa get than precious if there were 75 items in the exam?"""
    total_items = 75
    lyssa_incorrect = int(0.2 * total_items)
    precious_incorrect = 12
    lyssa_correct = total_items - lyssa_incorrect
    precious_correct = total_items - precious_incorrect
    more_correct = lyssa_correct - precious_correct
    result = more_correct
    return result

print(solution())