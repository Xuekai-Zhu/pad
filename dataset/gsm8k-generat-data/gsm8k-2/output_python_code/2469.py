def solution():
    """David and Brenda are playing Scrabble. Brenda is ahead by 22 points when she makes a 15-point play. David responds with a 32-point play. By how many points is Brenda now ahead?"""
    brenda_points = 0
    david_points = 0
    brenda_points += 15
    david_points += 32
    brenda_points += 22
    brenda_lead = brenda_points - david_points
    result = brenda_lead
    return result

print(solution())