def solution():
    """Lyssa and Precious took an English proficiency exam. Lyssa answered 20% of the items incorrectly. Precious got 12 mistakes. How many more correct answers did Lyssa get than precious if there were 75 items in the exam?"""
    # Define the total number of items in the exam and the percentage of incorrect answers by Lyssa
    total_items = 75
    lyssa_incorrect_percentage = 0.2

    # Calculate the number of incorrect answers by Lyssa and the number of correct ones
    lyssa_incorrect = total_items * lyssa_incorrect_percentage
    lyssa_correct = total_items - lyssa_incorrect

    # Calculate the number of correct answers by Precious
    precious_correct = total_items - 12

    # Calculate the difference in the number of correct answers between Lyssa and Precious
    answer_difference = lyssa_correct - precious_correct

    result = answer_difference
    return result

print(solution())