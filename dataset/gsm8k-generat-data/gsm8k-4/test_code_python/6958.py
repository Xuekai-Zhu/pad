def solution():
    """Together, Alan and Marcy handed out 150 parking tickets. If Marcy handed out 6 fewer than 5 times as many tickets as Alan, how many tickets did Alan hand out?"""
    
    # Initialize the number of tickets Alan handed out
    alan_tickets = 0
    
    # Calculate the number of tickets Marcy handed out using the given relationship
    marcy_tickets = 5 * alan_tickets - 6
    
    # Calculate the total number of tickets handed out
    total_tickets = alan_tickets + marcy_tickets
    
    # Use a loop to find the value of alan_tickets that satisfies the given conditions
    while total_tickets != 150:
        # Increment the number of tickets Alan handed out
        alan_tickets += 1
        
        # Calculate the number of tickets Marcy handed out using the given relationship
        marcy_tickets = 5 * alan_tickets - 6
        
        # Calculate the total number of tickets handed out
        total_tickets = alan_tickets + marcy_tickets
    
    # Return the number of tickets Alan handed out
    result = alan_tickets
    return result

print(solution())