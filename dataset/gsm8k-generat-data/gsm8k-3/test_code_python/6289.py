def solution():
    """Carly recently graduated and is looking for work in a field she studied for. She sent 200 job applications to companies in her state, and twice that number to companies in other states. Calculate the total number of job applications she has sent so far."""
    # Define the number of applications sent to companies in her state
    in_state = 200
    
    # Calculate the number of applications sent to companies in other states
    out_of_state = 2 * in_state
    
    # Calculate the total number of job applications sent
    total_applications = in_state + out_of_state
    
    result = total_applications
    return result

print(solution())