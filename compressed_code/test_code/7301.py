def solution():
    
    total_kids = 40
    fast_finishers = total_kids * 0.1
    faster_finishers = fast_finishers * 3
    remaining_kids = total_kids - fast_finishers - faster_finishers
    slow_finishers = remaining_kids / 6
    result = slow_finishers
    return result

print(solution())