def solution():
    
    # Define the amount of line needed for every foot of dock
    LINE_PER_DROCK = 3

    # Define the amount of dock and the amount of new line
    DROCK = 200
    NEW_LINE = 6

    # Calculate the total amount of line needed
    total_line = LINE_PER_DROCK * DROCK + NEW_LINE

    # Display the total amount of line needed
    result = total_line
    return result

print(solution())