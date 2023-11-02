def solution():
    """Hannah wants to get the highest grade in the class on the upcoming math test. Because she is out sick the day of the test, she learns ahead of time the top scores she has to beat. She finds out that one student got a 95% on the exam. Another student only got 3 wrong out of 40. How many questions does she have to get right to have the highest score in the class?"""
    # Calculate the total number of questions on the test
    total_questions = 40

    # Calculate the max number of questions Hannah can get wrong
    max_wrong = int(0.05 * total_questions)

    # Calculate the highest possible score she can get
    highest_score = (total_questions - max_wrong) / total_questions * 100

    # Calculate the number of questions she needs to get right
    num_right = int(highest_score / 100 * total_questions)

    # Display the number of questions she needs to get right
    result = num_right
    return result

print(solution())