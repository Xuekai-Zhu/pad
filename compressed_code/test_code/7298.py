def solution():
    
    pipe_length = 40
    bolts_needed = pipe_length // 5
    washers_needed = bolts_needed * 2
    washers_remaining = 20 - washers_needed
    result = washers_remaining
    return result

print(solution())