def solution():
    brenda_current_score = 22 + 15  # Brenda was already ahead by 22 points, and then she made a 15-point play
    david_current_score = brenda_current_score - 32  # David responded with a 32-point play, so his current score is subtracted from Brenda's current score

    # Calculate how many points Brenda is now ahead
    points_ahead = brenda_current_score - david_current_score
    result = points_ahead
    return result

print(solution())