def solution():
    total_students = 250

    basketball_percentage = 0.4
    basketball_students = total_students * basketball_percentage

    chess_percentage = 0.1
    chess_students = total_students * chess_percentage

    soccer_percentage = 0.28
    soccer_students = total_students * soccer_percentage

    badminton_students = total_students - basketball_students - chess_students - soccer_students

    # Calculate the number of students who identified chess or basketball as their favorite sport
    chess_or_basketball_students = basketball_students + chess_students
    result = chess_or_basketball_students
    return result

print(solution())