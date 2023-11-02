def solution():
    """There were 200 students on a field playing football. Suddenly a military plane flew by, and 3/4 of the students looked up. How many eyes saw the airplane?"""
    # Define the total number of students and the fraction of students who looked up
    total_students = 200
    looked_up_fraction = 3/4

    # Calculate the number of students who looked up
    looked_up_students = total_students * looked_up_fraction

    # Calculate the total number of eyes that saw the airplane (assuming all students have 2 eyes)
    total_eyes = looked_up_students * 2

    # Return the result
    result = total_eyes
    return result

print(solution())