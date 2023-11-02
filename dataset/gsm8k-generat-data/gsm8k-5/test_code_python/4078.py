def solution():
    # Calculate the number of girls at the beginning of the year
    girls_at_beginning = 15 * 1.2  # 20% greater than the number of boys

    # Calculate the total number of students at the beginning of the year
    students_at_beginning = 15 + girls_at_beginning

    # Calculate the new number of girls after the transfer students were admitted
    new_girls = girls_at_beginning * 2  # Number of girls doubled

    # Calculate the total number of students after the transfer students were admitted
    total_students = 15 + new_girls  # Number of boys remained the same

    result = total_students
    return result

print(solution())