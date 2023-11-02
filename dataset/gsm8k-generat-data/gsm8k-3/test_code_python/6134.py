def solution():
    """There were 200 students on a field playing football. Suddenly a military plane flew by, and 3/4 of the students looked up. How many eyes saw the airplane?"""
    # Define the total number of students and the fraction that looked up
    total_students = 200
    looked_up_fraction = 3/4

    # Calculate the number of students who looked up
    looked_up_students = total_students * looked_up_fraction

    # Calculate the number of eyes that saw the airplane
    eyes_seen = looked_up_students * 2  # assuming each student has two eyes

    # Display the number of eyes that saw the airplane
    result = eyes_seen
    return result

print(solution())