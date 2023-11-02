def solution():
    """On the night of the dance, 400 students show up to the party. 70% of the students who showed up were invited. If 40% of those invited to the party had their invitation revoked and were not allowed into the party, how many invited students attended the party?"""
    # Define the number of students who showed up and the percentage of invited students who attended
    total_students = 400
    invited_percentage = 0.7

    # Calculate the number of invited students who showed up
    invited_students = total_students * invited_percentage

    # Calculate the number of invited students who had their invitation revoked and were not allowed into the party
    revoked_percentage = 0.4
    revoked_students = invited_students * revoked_percentage

    # Calculate the number of invited students who attended the party
    attended_students = invited_students - revoked_students

    # Display the number of invited students who attended the party
    result = attended_students
    return result

print(solution())