def solution():
    # Let Maiya's age be x
    x = 4
    
    # Calculate the age of Maiya's first sister
    sister1 = 2*x + 1
    
    # Calculate the age of Maiya's second sister
    sister2 = 3*x - 1
    
    # Calculate the average age of the three sisters
    average_age = (x + sister1 + sister2) / 3
    
    # Check if the average age is 5
    if average_age == 5:
        result = x
    else:
        # If the average age is not 5, return an error message
        result = "Error: the average age is not 5"
    return result

print(solution())