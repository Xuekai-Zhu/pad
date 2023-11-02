def solution():
    """Lyssa and Precious took an English proficiency exam. Lyssa answered 20% of the items incorrectly. Precious got 12 mistakes. How many more correct answers did Lyssa get than precious if there were 75 items in the exam?"""
    total_items = 75
    lyssa_incorrect = int(total_items * 0.2) # converting to integer as Lyssa can't answer a fraction of a question
    precious_incorrect = 12
    lyssa_correct = total_items - lyssa_incorrect
    precious_correct = total_items - precious_incorrect
    difference = lyssa_correct - precious_correct
    result = difference
    return result

print(solution())