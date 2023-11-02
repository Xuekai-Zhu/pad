def solution():
    """Hilton had a box of 26 marbles that he was playing with.  He found 6 marbles while he was playing, but afterward realized that he had lost 10 marbles.  Lori felt bad and gave Hilton twice as many marbles as he lost.  How many marbles did Hilton have in the end?"""
    
    # Define the starting number of marbles
    starting_marbles = 26
    
    # Hilton found some marbles
    found_marbles = 6
    
    # Hilton lost some marbles
    lost_marbles = 10
    
    # Lori gave Hilton some marbles as an apology
    lori_gave = lost_marbles * 2
    
    # Calculate the total number of marbles
    total_marbles = starting_marbles + found_marbles - lost_marbles + lori_gave
    
    # Display the total number of marbles
    result = total_marbles
    return result

print(solution())