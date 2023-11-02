def solution():
    # Define the waiting times for each appointment and for the vaccine to be effective
    first_appt = 4
    second_appt = 20
    effective_wait = 14

    # Calculate the total waiting time
    total_wait = first_appt + second_appt + effective_wait
    result = total_wait
    return result

print(solution())