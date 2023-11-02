def solution():
    """In a 100-item exam, Lowella got 35% of the questions correctly. Pamela got 20% more correct answers than Lowella and Mandy got twice Pamela's score. 
    What is Mandy’s score?"""
    # Define the number of items in the exam
    total_items = 100

    # Calculate the number of correct answers Lowella got
    lowella_correct = total_items * 0.35

    # Calculate the number of correct answers Pamela got
    pamela_correct = lowella_correct * 1.2

    # Calculate the number of correct answers Mandy got
    mandy_correct = pamela_correct * 2

    # Calculate Mandy's score as a percentage
    mandy_score = (mandy_correct / total_items) * 100

    # return the result
    result = mandy_score
    return result

print(solution())