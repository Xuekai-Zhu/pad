def solution():
    """In a 100-item exam, Lowella got 35% of the questions correctly. Pamela got 20% more correct answers than Lowella and Mandy got twice Pamela's score. What is Mandy’s score?"""
    # Define the number of items in the exam
    EXAM_ITEMS = 100

    # Calculate Lowella's score
    lowella_score = 0.35 * EXAM_ITEMS

    # Calculate Pamela's score
    pamela_score = 1.2 * lowella_score

    # Calculate Mandy's score
    mandy_score = 2 * pamela_score

    # Display Mandy's score
    result = mandy_score
    return result

print(solution())