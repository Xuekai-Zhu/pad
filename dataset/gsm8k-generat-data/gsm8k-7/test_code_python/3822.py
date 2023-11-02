def solution():
    num_students = 60
    percent_needed = 0.75

    # Calculate the total number of votes needed to reach the goal
    goal_votes = num_students * percent_needed

    # Calculate the number of votes Alec already has
    initial_votes = num_students / 2

    # Calculate the number of votes from students who are thinking about voting for Alec
    possible_votes = 5

    # Update Alec's flyers to address issues of students who are thinking about voting for someone else
    updated_possible_votes = possible_votes / 5

    # Calculate the total number of votes Alec has after updating his flyers
    total_votes = initial_votes + updated_possible_votes

    # Calculate the number of additional votes Alec needs to reach his goal
    additional_votes_needed = goal_votes - total_votes
    result = additional_votes_needed
    return result

print(solution())