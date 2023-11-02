def solution():
    """Brenda picks 250 peaches. When she sorts through them, only 60% are fresh, and Brenda has to throw 15 away for being too small. How many peaches does Brenda have left?"""
    # Define the initial number of peaches Brenda picked
    initial_peaches = 250
    
    # Calculate the number of fresh peaches
    fresh_peaches = initial_peaches * 0.6
    
    # Calculate the number of peaches Brenda has left after throwing some away
    remaining_peaches = fresh_peaches - 15
    
    # Display the number of peaches Brenda has left
    result = remaining_peaches
    return result

print(solution())