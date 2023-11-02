def solution():
    """On the night of the dance, 400 students show up to the party. 70% of the students who showed up were invited. If 40% of those invited to the party had their invitation revoked and were not allowed into the party, how many invited students attended the party?"""
    # Define the total number of students who showed up
    total_students = 400

    # Calculate the number of invited students who showed up
    invited_students = total_students * 0.7

    # Calculate the number of invited students whose invitations were revoked
    revoked_students = invited_students * 0.4

    # Calculate the number of invited students who attended the party
    attended_students = invited_students - revoked_students

    # return the result
    result = attended_students
    return result

print(solution())