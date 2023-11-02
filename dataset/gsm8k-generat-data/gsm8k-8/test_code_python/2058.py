def solution():
    # Calculate Jay's score
    jay_score = 4 + 6

    # Calculate Tobee and Jay's score together
    tobee_jay_score = 4 + jay_score

    # Calculate Sean's score
    sean_score = tobee_jay_score - 2

    # Calculate the total score for the team
    total_score = tobee_jay_score + sean_score

    result = total_score
    return result

print(solution())