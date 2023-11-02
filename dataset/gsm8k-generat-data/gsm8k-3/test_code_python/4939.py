def solution():
    """Five percent of the 300 senior students got a full merit college scholarship and ten percent of them got a half merit scholarship. How many senior students did not get any scholarships?"""
    # Define the total number of senior students
    TOTAL_STUDENTS = 300

    # Calculate the number of students who received a full merit scholarship
    full_scholarship = int(TOTAL_STUDENTS * 0.05)

    # Calculate the number of students who received a half merit scholarship
    half_scholarship = int(TOTAL_STUDENTS * 0.1)

    # Calculate the number of students who did not receive any scholarships
    no_scholarship = TOTAL_STUDENTS - full_scholarship - half_scholarship

    # Display the number of students who did not receive any scholarships
    result = no_scholarship
    return result

print(solution())