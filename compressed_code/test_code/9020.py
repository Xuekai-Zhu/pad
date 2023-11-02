def solution():
    
    total_cases = 17
    dismissed_cases = 2
    remaining_cases = total_cases - dismissed_cases
    innocent_cases = remaining_cases * 2 / 3
    delayed_cases = 1
    guilty_cases = remaining_cases - innocent_cases - delayed_cases
    result = guilty_cases
    return result

print(solution())