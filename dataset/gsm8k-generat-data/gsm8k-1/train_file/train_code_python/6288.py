def solution():
    """Carly recently graduated and is looking for work in a field she studied for. She sent 200 job applications to companies in her state, and twice that number to companies in other states. Calculate the total number of job applications she has sent so far."""
    applications_within_state = 200
    applications_outside_state = 2 * applications_within_state
    total_applications = applications_within_state + applications_outside_state
    result = total_applications
    
    return result

print(solution())