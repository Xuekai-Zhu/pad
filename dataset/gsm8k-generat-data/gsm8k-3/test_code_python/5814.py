def solution():
    """Hillary's teacher assigned 1 hour of reading during the weekend. On Friday night, Hillary read for 16 minutes. On Saturday she read for 28 minutes. How many minutes does Hillary have to read on Sunday to complete the assignment?"""
    # Define the total reading time assigned in minutes
    TOTAL_TIME = 60

    # Calculate the total time read so far
    time_read = 16 + 28

    # Calculate the remaining reading time
    time_remaining = TOTAL_TIME - time_read

    # Display the remaining reading time in minutes
    result = time_remaining
    return result

print(solution())