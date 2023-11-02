def solution():
    
    # Define the length of Movie C in minutes
    C_LENGTH = 1.25 * 60

    # Calculate the length of Movie B in minutes
    B_LENGTH = C_LENGTH + 5

    # Calculate the length of Movie A in minutes
    A_LENGTH = B_LENGTH / 4

    # Display the length of Movie A in minutes
    result = A_LENGTH
    return result

print(solution())