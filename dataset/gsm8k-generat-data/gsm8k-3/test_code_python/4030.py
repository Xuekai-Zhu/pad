def solution():
    """In the beginning, Justine had 10 more rubber bands than Bailey but 2 fewer bands than Ylona. Bailey decided to give two bands each to Justine and Ylona so that he is left with only 8 rubber bands. How many rubber bands did Ylona have in the beginning?"""
    # Let Bailey have b rubber bands in the beginning
    b = 0
    # Justine has 10 more rubber bands than Bailey
    j = b + 10
    # Ylona has 2 more rubber bands than Justine
    y = j + 2
    
    # Bailey gave 2 rubber bands each to Justine and Ylona
    b -= 4
    j += 2
    y += 2
    
    # Bailey is left with 8 rubber bands
    b += 8
    
    # Solve for Ylona's original number of rubber bands
    y_orig = y - 4 - b
    
    # Display Ylona's original number of rubber bands
    result = y_orig
    return result

print(solution())