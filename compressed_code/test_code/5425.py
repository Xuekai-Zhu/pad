def solution():
    
    leak_rate = 1.5  
    time = 12  
    total_leak = leak_rate * time
    bucket_size = total_leak * 2
    result = bucket_size
    return result

print(solution())