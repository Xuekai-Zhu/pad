def solution():
    """Of the 24 students in class, one-third are in the after-school chess program, and half of those students will be absent from school on Friday for the regional chess tournament. How many of the students in this class are going to that tournament?"""
    total_students = 24
    chess_students = total_students / 3
    tournament_students = chess_students / 2
    result = tournament_students
    return result

print(solution())