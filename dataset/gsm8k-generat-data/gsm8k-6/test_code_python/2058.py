def solution():
    # Find how many points Jay scored
    jay_score = 4 + 6

    # Find the total points Tobee and Jay scored together
    tobee_jay_score = 4 + jay_score

    # Find how many points Sean scored
    sean_score = tobee_jay_score - 2

    # Find the total points the three scored for their team
    total_score = 4 + jay_score + sean_score

    return total_score

print(solution())