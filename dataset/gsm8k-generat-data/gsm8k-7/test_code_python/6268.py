def solution():
    accounting_time = 7
    total_time = 560
    
    # Calculate the ratio of accounting time to client calling time
    total_ratio = accounting_time + 1
    
    # Calculate the fraction of time spent calling clients
    client_calling_frac = 1 / total_ratio
    
    # Calculate the actual time spent calling clients
    client_calling_time = total_time * client_calling_frac
    result = client_calling_time
    return result

print(solution())