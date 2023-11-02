def solution():
    """Hillary's teacher assigned 1 hour of reading during the weekend. On Friday night, Hillary read for 16 minutes. On Saturday she read for 28 minutes. How many minutes does Hillary have to read on Sunday to complete the assignment?"""
    # Define the amount of time assigned and the time already read
    assigned_time = 60
    time_read = 16 + 28

    # Calculate the time remaining to complete the assignment
    time_remaining = assigned_time - time_read

    # Return the result
    result = time_remaining
    return result

print(solution())