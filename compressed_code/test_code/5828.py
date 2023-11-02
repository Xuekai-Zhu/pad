def solution():
    
    total_butter = 10
    butter_used_cc = total_butter / 2
    butter_used_pb = total_butter / 5
    butter_remaining = total_butter - butter_used_cc - butter_used_pb
    butter_used_sc = butter_remaining / 3
    butter_remaining -= butter_used_sc
    result = butter_remaining
    return result

print(solution())