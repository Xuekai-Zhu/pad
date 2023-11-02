def solution():
    # Define the number of students and instructors
    students = 40
    instructors = 10
    total_people = students + instructors

    # Calculate the number of students bringing life vests
    vest_students = int(students * 0.2)

    # Calculate the total number of vests needed
    total_vests_needed = total_people - vest_students

    # Calculate the number of additional vests needed
    additional_vests_needed = total_vests_needed - 20

    result = additional_vests_needed
    return result

print(solution())