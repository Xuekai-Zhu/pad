def solution():
    """In the beginning, Justine had 10 more rubber bands than Bailey but 2 fewer bands than Ylona.
    Bailey decided to give two bands each to Justine and Ylona so that he is left with only 8 rubber bands.
    How many rubber bands did Ylona have in the beginning?"""
    
    # Let's assume Bailey had x rubber bands initially
    x = 0
    
    # Justine had 10 more than Bailey
    j = x + 10
    
    # Ylona had 2 more than Justine
    y = j + 2
    
    # Bailey gives 2 bands each to Justine and Ylona
    j += 2
    y += 2
    
    # Bailey is left with 8 rubber bands
    x = 8
    
    # Total number of rubber bands initially
    initial_total_bands = j + y + x
    
    result = y
    
    return result

print(solution())