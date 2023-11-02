def solution():
    """A class of 12 students was about to share 108 oranges equally among themselves when it was discovered that 36 of the oranges were bad and had to be thrown away. How many oranges less will each student get now than if no orange had to be thrown away?"""
    # Define the number of students and oranges
    num_students = 12
    num_oranges = 108

    # Calculate the number of oranges for each student
    oranges_per_student = num_oranges // num_students

    # Remove the bad oranges
    num_bad_oranges = 36
    num_oranges -= num_bad_oranges

    # Calculate the number of oranges for each student after bad oranges were thrown away
    oranges_per_student_after = num_oranges // num_students

    # Calculate the difference in oranges per student
    oranges_lost = oranges_per_student - oranges_per_student_after

    # Display the difference in oranges per student
    result = oranges_lost
    return result

print(solution())