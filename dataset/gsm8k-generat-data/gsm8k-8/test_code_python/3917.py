def solution():
    # Define the time Jack had to wait
    customs_wait_time = 20
    quarantine_time = 14 * 24  # convert days to hours

    # Calculate the total time Jack had to wait
    total_wait_time = customs_wait_time + quarantine_time
    result = total_wait_time
    return result

print(solution())