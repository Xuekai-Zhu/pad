def solution():
    total_students = 24  # There are 24 students in class
    chess_students = total_students // 3  # One-third of the students are in the chess program
    tournament_absentees = chess_students // 2  # Half of the chess students are absent for the tournament

    # Calculate the number of students going to the tournament
    tournament_attendees = chess_students - tournament_absentees
    result = tournament_attendees
    return result

print(solution())