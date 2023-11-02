def solution():
    """In a survey about the student's favorite sports, 40% said they like basketball, 10% like chess, 28% like soccer, and the rest said they like badminton. If 250 students were interviewed, how many students identified chess or basketball as their favorite sport?"""
    # Define the percentage of students who like basketball, chess, and soccer
    basketball_percent = 40
    chess_percent = 10

    # Calculate the number of students who like basketball, chess, and soccer
    basketball_students = int(0.01 * basketball_percent * 250)
    chess_students = int(0.01 * chess_percent * 250)

    # Determine the total number of students who identified basketball or chess as their favorite sport
    total_students = basketball_students + chess_students

    # Display the total number of students
    result = total_students
    return result

print(solution())