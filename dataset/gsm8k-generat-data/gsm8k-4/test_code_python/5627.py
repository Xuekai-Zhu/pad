def solution():
    """Genevieve is a computer programmer working on information security software. She has written 4300 lines of code so far. Every 100 lines of code, she debugs the program. If each debugging only finds three errors, and Genevieve fixes the errors each time before proceeding, how many errors has she fixed so far?"""
    # Define the number of lines of code Genevieve has written so far
    lines_of_code = 4300

    # Calculate the number of times Genevieve has debugged the program
    debugs = lines_of_code // 100

    # Calculate the total number of errors Genevieve has fixed
    errors_fixed = debugs * 3

    # Return the result
    result = errors_fixed
    return result

print(solution())