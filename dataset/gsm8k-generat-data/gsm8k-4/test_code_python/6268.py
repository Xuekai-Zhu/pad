def solution():
    """Maryann spends seven times as long doing accounting as calling clients. If she worked 560 minutes today, how many minutes did she spend calling clients?"""
    # Define the ratio of time spent on accounting to time spent calling clients
    accounting_to_calling = 7
    
    # Calculate the total time spent
    total_time = 560
    
    # Calculate the total time spent on accounting
    accounting_time = total_time / (1 + accounting_to_calling)
    
    # Calculate the total time spent calling clients
    calling_time = total_time - accounting_time
    
    # Return the time spent calling clients
    result = calling_time
    return result

print(solution())