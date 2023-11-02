def solution():
    
    temp_temp = 32
    burn_per_log = 5
    temp_difference = 45 - 33
    logs_needed = (temp_diff - temp_temp) / burn_per_log
    result = logs_needed
    return result

print(solution())