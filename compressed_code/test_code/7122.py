def solution():
    
    time_to_SF_from_NY = 24
    time_to_NY_from_NO = (3/4) * time_to_SF_from_NY
    total_time = time_to_SF_from_NY + time_to_NY_from_NO + 16
    result = total_time
    return result

print(solution())