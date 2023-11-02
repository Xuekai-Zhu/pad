def solution():
    # Calculate the total number of classes in each school
    classes_per_school = 4 + 5

    # Calculate the total number of soccer balls to donate per school
    soccer_balls_per_school = 5 * classes_per_school

    # Calculate the total number of soccer balls to donate in both schools
    total_soccer_balls = soccer_balls_per_school * 2

    result = total_soccer_balls
    return result

print(solution())