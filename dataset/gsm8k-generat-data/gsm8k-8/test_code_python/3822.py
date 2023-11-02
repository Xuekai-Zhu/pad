def solution():
    # Calculate the total number of students who haven't said they'll vote for Alec
    remaining_students = 60 - 30 - 5  # half the class + students thinking about voting for Alec

    # Calculate the number of students in the remaining group who might vote for Alec
    potential_voters = remaining_students / 5  # one-fifth of students thinking about voting for someone else

    # Calculate the number of votes Alec needs to reach his goal
    goal_votes = 0.75 * 60  # three-quarters of the class
    current_votes = 30 + 5 + potential_voters
    needed_votes = goal_votes - current_votes

    result = needed_votes
    return result

print(solution())