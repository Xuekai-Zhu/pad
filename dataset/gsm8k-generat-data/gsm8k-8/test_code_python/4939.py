def solution():
    # Define the total number of senior students
    total_students = 300

    # Calculate the number of senior students who got full merit scholarships
    full_scholarship_students = 0.05 * total_students

    # Calculate the number of senior students who got half merit scholarships
    half_scholarship_students = 0.1 * total_students

    # Calculate the number of senior students who did not get any scholarships
    no_scholarship_students = total_students - full_scholarship_students - half_scholarship_students

    result = no_scholarship_students
    return result

print(solution())