def solution():
    """There are 20 students in the class. Half of them play basketball. Two-fifths play volleyball and one-tenth play both basketball and volleyball. How many students in this class do not play either game?"""
    # Define the total number of students and the fractions who play each game
    total_students = 20
    basketball_fraction = 0.5
    volleyball_fraction = 0.4
    both_fraction = 0.1

    # Calculate the number of students who play basketball only
    basketball_only = total_students * basketball_fraction - total_students * both_fraction

    # Calculate the number of students who play volleyball only
    volleyball_only = total_students * volleyball_fraction - total_students * both_fraction

    # Calculate the number of students who do not play either game
    neither = total_students - basketball_only - volleyball_only - total_students * both_fraction

    # return the result
    result = neither
    return result

print(solution())