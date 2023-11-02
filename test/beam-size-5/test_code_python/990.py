def solution():
    
    tobias_time = 20
    chikote_time = tobias_time * 2
    igneous_time = (tobias_time + chikote_time) / 2
    total_time = tobias_time + chikote_time + igneous_time
    time_in_minutes = total_time * 60
    result = time_in_minutes
    return result

print(solution())