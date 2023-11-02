def solution():
    class_size = 60  # Alec's class has 60 students
    votes_needed = class_size * (3/4)  # Alec needs three-quarters of the class, or 45 votes, to win
    current_votes = 30  # Half of the class, or 30 students, have already said they will vote for Alec
    potential_votes = 5  # 5 students are thinking about voting for Alec
    updated_potential_votes = potential_votes / 5  # After changing his flyers, 1/5 of these students say they will vote for Alec
    updated_total_votes = current_votes + updated_potential_votes  # Alec's current total number of votes
    votes_needed - updated_total_votes  # Calculate how many more votes Alec needs to reach his goal
    result = votes_needed - updated_total_votes
    return result

print(solution())