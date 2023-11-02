def solution():
    # Calculate the number of students who need life vests
    students = 40 - 1  # Alice is also a student, so we subtract her from the total number of students
    students_with_lifevests = int(0.2 * students)  # 20% of students are bringing life vests
    students_without_lifevests = students - students_with_lifevests

    # Calculate the number of life vests needed
    lifevests_needed = students_without_lifevests + 10  # 10 instructors also need life vests

    # Calculate the number of additional life vests Alice needs to get
    additional_lifevests = lifevests_needed - 20  # Alice already has 20 life vests

    result = additional_lifevests
    return result

print(solution())