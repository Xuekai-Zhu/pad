def solution():
    # Calculate the number of invited students
    invited_students = 400 * 0.7

    # Calculate the number of invited students who were not allowed into the party
    revoked_students = invited_students * 0.4

    # Calculate the number of invited students who attended the party
    attending_students = invited_students - revoked_students
    result = attending_students
    return result

print(solution())