def solution():
    # Setup the equation based on given information
    # Let E be the amount of dollars Evan earned
    # Markese earned 5 fewer dollars than Evan -> Markese earned E-5 dollars
    # Together they earned $37 -> E + (E-5) = 37
    
    E = None  # Initialize E to None
    for i in range(1, 37):  # Iterate over possible E values from 1 to 36 (since Markese has to earn at least 1 dollar)
        if i + (i-5) == 37:  # If the equation is satisfied, assign E to i and break the loop
            E = i
            break
    
    # Markese earned E-5 dollars
    Markese_earned = E - 5
    result = Markese_earned
    return result

print(solution())