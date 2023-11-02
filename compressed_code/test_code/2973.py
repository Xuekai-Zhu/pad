def solution():
    
    total_students = 60
    vote_goal = 0.75 * total_students
    initial_votes = 0.5 * total_students + 5
    changed_flyers_votes = (1/5) * (total_students - initial_votes)
    total_votes = initial_votes + changed_flyers_votes
    additional_votes_needed = vote_goal - total_votes
    result = additional_votes_needed
    return result

print(solution())