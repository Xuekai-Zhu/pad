def solution():
    """Lyssa and Precious took an English proficiency exam. Lyssa answered 20% of the items incorrectly. Precious got 12 mistakes. How many more correct answers did Lyssa get than precious if there were 75 items in the exam?"""
    # Define the total number of items in the exam
    total_items = 75

    # Calculate the number of items Lyssa answered incorrectly
    lyssa_incorrect = int(0.2 * total_items)

    # Calculate the number of items Lyssa answered correctly
    lyssa_correct = total_items - lyssa_incorrect

    # Calculate the number of items Precious answered correctly
    precious_correct = total_items - 12

    # Calculate the difference in the number of correct answers between Lyssa and Precious
    correct_difference = lyssa_correct - precious_correct

    # Display the difference in the number of correct answers
    result = correct_difference
    return result

print(solution())