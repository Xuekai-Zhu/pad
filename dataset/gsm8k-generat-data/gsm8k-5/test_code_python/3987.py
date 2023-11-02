def solution():
    total_students = 250  # 250 students were interviewed
    basketball_percentage = 40  # 40% of students like basketball
    chess_percentage = 10  # 10% of students like chess
    soccer_percentage = 28  # 28% of students like soccer

    # Calculate the number of students who like basketball
    basketball_students = (basketball_percentage / 100) * total_students

    # Calculate the number of students who like chess
    chess_students = (chess_percentage / 100) * total_students

    # Calculate the total number of students who like basketball or chess
    total_basketball_or_chess_students = basketball_students + chess_students

    result = total_basketball_or_chess_students
    return result

print(solution())