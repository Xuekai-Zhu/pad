def solution():
    """A class of 12 students was about to share 108 oranges equally among themselves when it was discovered that 36 of the oranges were bad and had to be thrown away. How many oranges less will each student get now than if no orange had to be thrown away?"""
    # Define the number of students and oranges
    students = 12
    oranges = 108

    # Calculate the number of oranges per student before any were thrown away
    oranges_per_student_before = oranges // students

    # Calculate the number of oranges that had to be thrown away
    bad_oranges = 36

    # Calculate the new number of oranges after the bad ones were thrown away
    oranges_after = oranges - bad_oranges

    # Calculate the number of oranges per student after some were thrown away
    oranges_per_student_after = oranges_after // students

    # Calculate the difference in the number of oranges per student
    difference = oranges_per_student_before - oranges_per_student_after

    # Return the result
    result = difference
    return result

print(solution())