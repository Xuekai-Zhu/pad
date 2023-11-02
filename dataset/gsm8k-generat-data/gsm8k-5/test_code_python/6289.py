def solution():
    in_state_applications = 200  # Carly sent 200 job applications to companies in her state
    out_of_state_applications = 2 * in_state_applications  # Carly sent twice as many job applications to companies in other states

    # Calculate the total number of job applications Carly has sent
    total_applications = in_state_applications + out_of_state_applications
    result = total_applications
    return result

print(solution())