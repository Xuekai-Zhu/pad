def solution():
    total_students = 300
    full_scholarship_percent = 0.05
    half_scholarship_percent = 0.1

    # Calculate the number of senior students who got a full scholarship
    num_full_scholarship_students = total_students * full_scholarship_percent

    # Calculate the number of senior students who got a half scholarship
    num_half_scholarship_students = total_students * half_scholarship_percent

    # Calculate the total number of senior students who got a scholarship
    num_scholarship_students = num_full_scholarship_students + num_half_scholarship_students

    # Calculate the number of senior students who did not get a scholarship
    num_no_scholarship_students = total_students - num_scholarship_students
    result = num_no_scholarship_students
    return result

print(solution())