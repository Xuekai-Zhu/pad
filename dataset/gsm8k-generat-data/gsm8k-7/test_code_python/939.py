def solution():
    num_students = 20
    basketball_percent = 0.5
    volleyball_percent = 0.4
    both_percent = 0.1

    # Calculate the number of students who play basketball only
    basketball_only = num_students * basketball_percent - num_students * both_percent

    # Calculate the number of students who play volleyball only
    volleyball_only = num_students * volleyball_percent - num_students * both_percent

    # Calculate the number of students who play both basketball and volleyball
    both = num_students * both_percent

    # Calculate the number of students who do not play either game
    neither = num_students - basketball_only - volleyball_only - both
    result = neither
    return result

print(solution())