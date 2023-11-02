def solution():
    """In a survey about the student's favorite sports, 40% said they like basketball, 10% like chess, 28% like soccer, and the rest said they like badminton. If 250 students were interviewed, how many students identified chess or basketball as their favorite sport?"""
    # Define the total number of students surveyed
    total_students = 250

    # Calculate the number of students who like basketball
    basketball_students = total_students * 0.4

    # Calculate the number of students who like chess
    chess_students = total_students * 0.1

    # Calculate the total number of students who like chess or basketball
    favorite_students = basketball_students + chess_students

    # return the result
    result = favorite_students
    return result

print(solution())