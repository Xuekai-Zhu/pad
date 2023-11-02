def solution():
    """In a survey about the student's favorite sports, 40% said they like basketball, 10% like chess, 28% like soccer, and the rest said they like badminton. If 250 students were interviewed, how many students identified chess or basketball as their favorite sport?"""
    total_students = 250
    basketball_percentage = 0.4
    chess_percentage = 0.1
    soccer_percentage = 0.28
    badminton_percentage = 1 - basketball_percentage - chess_percentage - soccer_percentage
    basketball_students = basketball_percentage * total_students
    chess_students = chess_percentage * total_students
    result = basketball_students + chess_students
    return result

print(solution())