def solution():
    total_students = 250
    basketball_percent = 40
    chess_percent = 10

    # Calculate the number of students who like basketball
    basketball_students = (basketball_percent/100) * total_students

    # Calculate the number of students who like chess
    chess_students = (chess_percent/100) * total_students

    # Calculate the total number of students who identified chess or basketball as their favorite sport
    total_favorite = basketball_students + chess_students
    result = total_favorite
    return result

print(solution())