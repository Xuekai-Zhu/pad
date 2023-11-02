def solution():
    total_students = 60  # total number of students in Alec's class
    votes_needed = (3/4) * total_students  # number of votes Alec needs to win
    current_votes = 0  # current number of votes Alec has
    current_votes += (1/2) * total_students  # half of the class has already said they will vote for him
    current_votes += 5  # 5 students are thinking about voting for him
    # Changing his flyers results in (1/5) of the students who were thinking about voting for someone else
    # saying they'll vote for him. So, we can add (1/5) * x to the current_votes, where x is the
    # number of students who were thinking about voting for someone else.
    x = total_students - current_votes
    current_votes += (1/5) * x
    additional_votes_needed = votes_needed - current_votes  # additional votes Alec needs to reach his goal
    result = additional_votes_needed
    return result

print(solution())