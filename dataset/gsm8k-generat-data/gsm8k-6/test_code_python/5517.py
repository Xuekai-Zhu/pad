def solution():
    # Convert Kwame and Connor's study times to minutes
    kwame_minutes = 2.5 * 60
    connor_minutes = 1.5 * 60
    
    # Calculate the total minutes studied by Kwame and Connor
    total_minutes = kwame_minutes + connor_minutes + 97
    
    # Calculate the difference in minutes between Kwame and Connor's total study time and Lexia's study time
    difference = total_minutes - 97
    
    result = difference
    return result

print(solution())