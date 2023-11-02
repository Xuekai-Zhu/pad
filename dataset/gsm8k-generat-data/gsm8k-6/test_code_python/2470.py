def solution():
    brenda_score = 0  # initialize Brenda's score
    david_score = 0  # initialize David's score
    brenda_score += 15  # Brenda makes a 15-point play
    brenda_score += 22  # Brenda was already ahead by 22 points
    david_score += 32  # David responds with a 32-point play
    point_difference = brenda_score - david_score  # calculate the difference in scores
    result = point_difference
    return result

print(solution())