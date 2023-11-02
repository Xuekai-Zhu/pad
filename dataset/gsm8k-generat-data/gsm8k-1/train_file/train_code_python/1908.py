def solution():
    """40 kids are running a race. 10% of them pass the finish line in less than 6 minutes. Three times that number finish in less than 8 minutes. 1/6 of the remaining kids take more than 14 minutes. How many kids take more than 14 minutes?"""
    total_kids = 40
    fast_finishers = total_kids * 0.1
    faster_finishers = fast_finishers * 3
    remaining_kids = total_kids - fast_finishers - faster_finishers
    slow_finishers = remaining_kids / 6
    result = slow_finishers
    return result

print(solution())