def solution():
    num_students = 24

    # Calculate the number of students in the after-school chess program
    chess_students = num_students / 3

    # Calculate the number of students in the after-school chess program who will be absent on Friday
    absent_students = chess_students / 2

    # Calculate the total number of students going to the tournament
    num_tournament_students = absent_students
    result = num_tournament_students
    return result

print(solution())