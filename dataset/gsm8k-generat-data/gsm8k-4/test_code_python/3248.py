def solution():
    """There are 180 students in ninth grade. 1/4 of them bombed their finals because they were going through difficult breakups. 1/3rd of the rest didn't show up to take the test, and another 20 got less than a D. How many students passed their finals?"""
    # Define the total number of students
    total_students = 180

    # Calculate the number of students who bombed their finals
    bombed_students = total_students * 0.25

    # Calculate the number of students who didn't show up
    no_show_students = (total_students - bombed_students) * (1/3)

    # Calculate the number of students who got less than a D
    less_than_d_students = 20

    # Calculate the number of students who passed their finals
    passed_students = total_students - bombed_students - no_show_students - less_than_d_students

    # Return the result
    result = passed_students
    return result

print(solution())