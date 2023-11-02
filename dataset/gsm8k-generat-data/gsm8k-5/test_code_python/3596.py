def solution():
    # Find the total number of students with brown eyes
    total_brown_eyes = 6 * 2  # Half of the students with brown eyes have black hair, so 6 is half of the total number of students with black hair and brown eyes
    brown_eye_ratio = 2/3  # Two-thirds of the students have brown eyes

    # Use a proportion to find the total number of students
    total_students = total_brown_eyes / (brown_eye_ratio * 0.5)

    result = int(total_students)
    return result

print(solution())