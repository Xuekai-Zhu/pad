def solution():
    """David and Brenda are playing Scrabble. Brenda is ahead by 22 points when she makes a 15-point play. David responds with a 32-point play. By how many points is Brenda now ahead?"""
    current_lead = 22
    brenda_play = 15
    david_play = 32
    brenda_lead = current_lead + brenda_play - david_play
    result = brenda_lead
    return result

print(solution())