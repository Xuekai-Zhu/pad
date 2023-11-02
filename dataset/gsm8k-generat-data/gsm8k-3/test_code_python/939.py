def solution():
    """There are 20 students in the class. Half of them play basketball. Two-fifths play volleyball and one-tenth play both basketball and volleyball.  How many students in this class do not play either game?"""
    # Define the number of students in the class
    total_students = 20

    # Calculate the number of students who play basketball
    basketball_players = total_students / 2

    # Calculate the number of students who play volleyball
    volleyball_players = total_students * (2/5)

    # Calculate the number of students who play both basketball and volleyball
    both_players = total_students / 10

    # Calculate the number of students who do not play either game
    neither = total_students - basketball_players - volleyball_players + both_players

    # Display the number of students who do not play either game
    result = neither
    return result

print(solution())