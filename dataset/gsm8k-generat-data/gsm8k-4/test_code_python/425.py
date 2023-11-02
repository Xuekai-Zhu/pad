def solution():
    """Calvin and Paislee played a pool game where points were awarded for winning a round. 
    If Calvin had scored 500 points and Paislee 3/4 times as many points as Calvin, 
    how many points was Paislee required to achieve to have a chance of tying the game?"""
    
    # Define Calvin's score and calculate Paislee's score
    calvin_score = 500
    paislee_score = (3/4) * calvin_score
    
    # Calculate how many more points Paislee needs to tie with Calvin
    points_needed = calvin_score - paislee_score
    
    # Return the result
    result = points_needed
    return result

print(solution())