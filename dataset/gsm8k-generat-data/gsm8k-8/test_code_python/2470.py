def solution():
    # Define Brenda's score before her 15-point play
    brenda_score_before = david_score + 22

    # Calculate Brenda's score after her 15-point play
    brenda_score_after = brenda_score_before + 15

    # Calculate David's score after his 32-point play
    david_score_after = david_score + 32

    # Calculate the difference between Brenda's and David's scores
    diff = brenda_score_after - david_score_after
    result = diff
    return result

print(solution())