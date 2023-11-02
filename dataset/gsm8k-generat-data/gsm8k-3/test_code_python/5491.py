def solution():
    """Of the 24 students in class, one-third are in the after-school chess program, and half of those students will be absent from school on Friday for the regional chess tournament. How many of the students in this class are going to that tournament?"""
    # Define the total number of students in the class
    total_students = 24

    # Calculate the number of students in the chess program
    chess_students = total_students / 3

    # Calculate the number of chess students who will be absent
    absent_chess_students = chess_students / 2

    # Calculate the number of students going to the tournament
    tournament_students = absent_chess_students

    # Display the number of students going to the tournament
    result = tournament_students
    return result

print(solution())