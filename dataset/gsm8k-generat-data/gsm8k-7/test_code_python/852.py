def solution():
    initial_ants = 50
    time_in_hours = 5

    # Calculate the final number of ants based on the exponential growth formula Nt = N0 * 2^t
    final_ants = initial_ants * (2 ** time_in_hours)
    result = final_ants
    return result

print(solution())