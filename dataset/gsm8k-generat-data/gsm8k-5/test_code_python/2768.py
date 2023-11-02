def solution():
    robert_balls = 25
    tim_balls = 40
    
    # Calculate how many balls Tim gave to Robert
    tim_to_robert = tim_balls / 2
    
    # Add the balls Tim gave to Robert to Robert's original balls
    robert_balls += tim_to_robert
    
    result = robert_balls
    return result

print(solution())