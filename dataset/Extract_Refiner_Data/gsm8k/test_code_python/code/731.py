def solution():
    
    total_voters = 100
    candidate_a_votes = total_voters * 0.2
    candidate_b_votes = candidate_a_votes * 1.5
    candidate_c_votes = total_voters - candidate_a_votes - candidate_b_votes
    result = candidate_c_votes
    return result

print(solution())