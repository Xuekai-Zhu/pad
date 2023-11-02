def solution():
    # Calculate the total number of job applications Carly sent
    in_state = 200
    out_of_state = 2 * in_state  # twice the number of applications to companies in other states
    total_applications = in_state + out_of_state
    result = total_applications
    return result

print(solution())