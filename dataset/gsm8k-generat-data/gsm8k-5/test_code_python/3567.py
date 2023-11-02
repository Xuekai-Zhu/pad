def solution():
    total_students = 400  # 400 students show up to the party
    invited_ratio = 0.7  # 70% of the students who showed up were invited
    allowed_ratio = 0.6  # 40% of the invited students were not allowed into the party

    # Calculate the total number of invited students
    invited_students = total_students / invited_ratio

    # Calculate the number of invited students allowed into the party
    allowed_students = invited_students * allowed_ratio

    result = allowed_students
    return result

print(solution())