def solution():
    """Five percent of the 300 senior students got a full merit college scholarship and ten percent of them got a half merit scholarship. How many senior students did not get any scholarships?"""
    # Define the total number of senior students
    total_students = 300

    # Calculate the number of students who received a full merit scholarship
    full_scholarship_students = total_students * 0.05

    # Calculate the number of students who received a half merit scholarship
    half_scholarship_students = total_students * 0.1

    # Calculate the number of students who did not receive any scholarships
    no_scholarship_students = total_students - full_scholarship_students - half_scholarship_students

    # Return the result
    result = no_scholarship_students
    return result

print(solution())