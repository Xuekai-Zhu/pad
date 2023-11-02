def solution():
    """Sally, Sam, and Steve went to play with their marbles. In the beginning, Sam has twice as many marbles as Steve while Sally has 5 less than Sam. After Sam has given Sally and Steve 3 marbles each, Sam has 8 marbles left. How many marbles does Steve have now?"""
    sam = 16  # assume Sam has 16 marbles in the beginning
    sally = sam - 5  # Sally has 5 less than Sam
    steve = sam / 2  # Sam has twice as many marbles as Steve
    
    sam -= 6  # Sam gives 3 marbles each to Sally and Steve
    sally += 3
    steve += 3
    
    # After giving away the marbles, Sam has 8 marbles left
    # So the total number of marbles in the beginning was:
    total_marbles = sam + sally + steve + 8
    
    # Now we need to find out how many marbles Steve has after the transaction
    # Let's first find out what percentage of the total marbles he had in the beginning:
    steve_percentage = steve / total_marbles
    
    # Steve will have the same percentage of the new total marbles as well
    # Let's assume the new total marbles is "x"
    # Then the equation would be: steve_percentage * x = steve
    # Solving for x:
    x = steve / steve_percentage
    
    # Now we know the new total number of marbles, and we know that Steve has
    # the same percentage of marbles as before, so we can find out how many
    # marbles he has now:
    steve_now = x * steve_percentage
    
    result = steve_now
    
    return result

print(solution())