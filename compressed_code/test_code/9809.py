def solution():
    
    total_needed = 45
    bought = total_needed / 3
    found = total_needed / 5
    still_needed = total_needed - (bought + found)
    result = still_needed
    return result

print(solution())