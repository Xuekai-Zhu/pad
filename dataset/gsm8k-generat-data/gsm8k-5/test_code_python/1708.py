def solution():
    # Mark's team scores
    team_score = (25*2) + (8*3) + 10

    # Opponent team scores
    opponent_2pt = 25*2*2  # double the 2 pointers
    opponent_3pt = 8*3/2   # half the 3 pointers
    opponent_ft = 10/2     # half the free throws
    opponent_score = opponent_2pt + opponent_3pt + opponent_ft 

    # Total score
    total_score = team_score + opponent_score
    result = total_score
    return result

print(solution())