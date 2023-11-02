def solution():
    """On the first day of school, Mrs. McGillicuddy had 25 students registered for the morning session of kindergarten, but 3 students were absent;
    and she had 24 students registered for the afternoon session, but 4 students were absent. How many students did Mrs. McGillicuddy have over the two kindergarten sessions?"""
    # Calculate the number of students present in the morning session by subtracting the number of absent students from the number registered
    morning_students = 25 - 3

    # Calculate the number of students present in the afternoon session by subtracting the number of absent students from the number registered
    afternoon_students = 24 - 4

    # Add the number of students present in both sessions to get the total number of students
    total_students = morning_students + afternoon_students

    # Return the result
    result = total_students
    return result

print(solution())