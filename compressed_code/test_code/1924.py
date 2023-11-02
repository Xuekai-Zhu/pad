def solution():
    
    total_sessions = 25
    patient1_sessions = 6
    patient2_sessions = patient1_sessions + 5
    remaining_sessions = total_sessions - patient1_sessions - patient2_sessions
    result = remaining_sessions
    return result

print(solution())