def solution():
    """In a Geometry exam, Madeline got 2 mistakes which are half as many mistakes as Leo. Brent scored 25 and has 1 more mistake than Leo. What is Madeline's score?"""
    # Define the number of mistakes made by Madeline and Leo
    madeline_mistakes = 2
    leo_mistakes = madeline_mistakes * 2

    # Define the number of mistakes made by Brent
    brent_mistakes = leo_mistakes + 1

    # Calculate the total number of correct answers for each student
    madeline_correct = 100 - madeline_mistakes
    leo_correct = 100 - leo_mistakes
    brent_correct = 100 - brent_mistakes

    # Calculate Madeline's score
    madeline_score = madeline_correct

    # return the result
    result = madeline_score
    return result

print(solution())