def solution():
    """A school has 1000 students. Half of the students were taken on a trip to the nearby beach. Half of the remaining students were sent home. How many students are still in the school?"""
    # Define the total number of students
    total_students = 1000

    # Calculate the number of students taken on the beach trip
    beach_students = total_students // 2

    # Calculate the number of students remaining after the beach trip
    remaining_students = total_students - beach_students

    # Calculate the number of students sent home
    sent_home_students = remaining_students // 2

    # Calculate the number of students still in the school
    students_still_in_school = remaining_students - sent_home_students

    # Display the number of students still in the school
    result = students_still_in_school
    return result

print(solution())