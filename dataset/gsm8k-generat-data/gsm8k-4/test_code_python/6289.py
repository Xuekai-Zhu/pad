def solution():
    """Carly recently graduated and is looking for work in a field she studied for. She sent 200 job applications to companies in her state, and twice that number to companies in other states. Calculate the total number of job applications she has sent so far."""
    # Define the number of job applications sent to in-state companies
    in_state = 200

    # Calculate the number of job applications sent to out-of-state companies
    out_state = 2 * in_state

    # Calculate the total number of job applications sent
    total = in_state + out_state

    result = total
    return result

print(solution())