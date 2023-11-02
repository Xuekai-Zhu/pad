def solution():
    """Amanda needs 12 more marbles to have twice as many marbles as Katrina, and Mabel has 5 times as many marbles as Katrina. If Mabel has 85 marbles, how many more marbles does Mabel have than Amanda?"""
    # Define the number of marbles Mabel has and the multiplier to find the number of marbles Katrina has
    MABEL_MARBLES = 85
    KATRINA_MULTIPLIER = 1/5
    
    # Calculate the number of marbles Katrina has
    katrina_marbles = MABEL_MARBLES * KATRINA_MULTIPLIER
    
    # Calculate the number of marbles Amanda has
    amanda_marbles = katrina_marbles * 2 - 12
    
    # Calculate the difference in the number of marbles between Mabel and Amanda
    difference = MABEL_MARBLES - amanda_marbles
    
    # Display the difference in the number of marbles between Mabel and Amanda
    result = difference
    return result

print(solution())