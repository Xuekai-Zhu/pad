def solution():
    """50% of substitute teachers walk out after 1 hour of teaching. 30% of the remainder quit before lunch. If 60 substitute teachers show up at 7 AM, how many will be left after lunch?"""
    # Define the initial number of substitute teachers
    initial_teachers = 60

    # Calculate the number of teachers who walk out after 1 hour
    walkout_teachers = initial_teachers * 0.5

    # Calculate the number of remaining teachers
    remaining_teachers = initial_teachers - walkout_teachers

    # Calculate the number of teachers who quit before lunch
    quit_teachers = remaining_teachers * 0.3

    # Calculate the number of teachers left after lunch
    final_teachers = remaining_teachers - quit_teachers

    # return the result
    result = final_teachers
    return result

print(solution())