def solution():
    """Sally, Sam, and Steve went to play with their marbles. In the beginning, Sam has twice as many marbles as Steve while Sally has 5 less than Sam. After Sam has given Sally and Steve 3 marbles each, Sam has 8 marbles left. How many marbles does Steve have now?"""
    # Define the initial number of marbles Sam has as s
    s = None
    
    # Define the number of marbles Steve has as x
    x = None
    
    # Define the number of marbles Sally has as y
    y = None
    
    # Set up the equations based on the given information
    
    # Sam has twice as many marbles as Steve
    s = 2*x
    
    # Sally has 5 less than Sam
    y = s - 5
    
    # Sam gave Sally and Steve 3 marbles each and had 8 left
    s = s - 3 - 3 - 8
    y = y + 3
    x = x + 3
    
    # Solve for x
    x = (s/2)
    
    # return the result
    result = x
    return result

print(solution())