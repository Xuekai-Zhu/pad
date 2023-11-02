def solution():
    # Define the time spent studying as one-third of the time spent playing video games
    study_time = 9 / 3

    # Calculate the number of points Jackson earns based on the time spent studying
    point_increase = 15 * study_time

    # Add the point increase to Jackson's starting grade of 0
    grade = 0 + point_increase
    result = grade
    return result

print(solution())