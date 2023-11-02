def solution():
    num_deaf_students = 180
    deaf_to_blind_ratio = 3

    # Calculate the number of blind students
    num_blind_students = num_deaf_students // deaf_to_blind_ratio

    # Calculate the total number of students
    total_students = num_deaf_students + num_blind_students
    result = total_students
    return result

print(solution())