def solution():
    """On the first day of school, Mrs. McGillicuddy had 25 students registered for the morning session of kindergarten, but 3 students were absent; and she had 24 students registered for the afternoon session, but 4 students were absent. How many students did Mrs. McGillicuddy have over the two kindergarten sessions?"""
    # Calculate the number of students present for the morning session
    morning_present = 25 - 3

    # Calculate the number of students present for the afternoon session
    afternoon_present = 24 - 4

    # Calculate the total number of students present over both sessions
    total_present = morning_present + afternoon_present

    # Display the total number of students present
    result = total_present
    return result

print(solution())