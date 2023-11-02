def solution():
    """Genevieve is a computer programmer working on information security software. She has written 4300 lines of code so far. Every 100 lines of code, she debugs the program. If each debugging only finds three errors, and Genevieve fixes the errors each time before proceeding, how many errors has she fixed so far?"""
    # Define the number of lines of code and errors per 100 lines
    LINES_PER_DEBUG = 100
    ERRORS_PER_DEBUG = 3

    # Calculate the number of debugs Genevieve has performed
    num_debugs = 4300 // LINES_PER_DEBUG

    # Calculate the total number of errors fixed
    total_errors_fixed = num_debugs * ERRORS_PER_DEBUG

    # Display the total number of errors fixed
    result = total_errors_fixed
    return result

print(solution())