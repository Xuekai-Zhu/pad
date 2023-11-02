def solution():
    """In a basketball game, Tobee scored 4 points. Jay scored 6 more than Tobee and Sean scored 2 less than the points of Tobee and Jay together. If Tobee, Jay, and Sean are on the same team, how many points did they score for their team?"""
    
    # Define Tobee's score
    tobee_score = 4
    
    # Calculate Jay's score
    jay_score = tobee_score + 6
    
    # Calculate Tobee and Jay's total score
    tobee_jay_total = tobee_score + jay_score
    
    # Calculate Sean's score
    sean_score = tobee_jay_total - 2
    
    # Calculate the total score for their team
    total_score = tobee_score + jay_score + sean_score
    
    # Display the total score
    result = total_score
    return result

print(solution())