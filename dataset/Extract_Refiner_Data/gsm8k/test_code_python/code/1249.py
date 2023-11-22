def solution():
    
    # Define the time Tim spends on work and the time it takes to deal with a call
    work_time = 6 * 60 * 5  # convert hours to minutes
    call_time = 15  # minutes

    # Calculate the number of calls Tim can deal with in the given time
    calls = work_time // call_time

    # return the result
    result = calls
    return result

print(solution())