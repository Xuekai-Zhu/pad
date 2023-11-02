def solution():
    """On the night of the dance, 400 students show up to the party. 70% of the students who showed up were invited. If 40% of those invited to the party had their invitation revoked and were not allowed into the party, how many invited students attended the party?"""
    total_students = 400
    invited_percentage = 0.7
    revoked_percentage = 0.4
    invited_students = total_students / invited_percentage
    actual_invited_students = invited_students * (1 - revoked_percentage)
    result = actual_invited_students
    return result

print(solution())