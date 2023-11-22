def solution():
    
    # Define the total number of teachers
    total_teachers = 150

    # Calculate the number of history teachers
    history_teachers = total_teachers * 0.6

    # Calculate the number of math teachers
    math_teachers = total_teachers - history_teachers

    # Calculate the total time spent sleeping math teachers
    total_sleeping_time = math_teachers * 6

    # return the result
    result = total_sleeping_time
    return result

print(solution())