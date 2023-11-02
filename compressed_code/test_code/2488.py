def solution():
    
    lines_per_sonnet = 14
    unheard_lines = 70
    total_lines = lines_per_sonnet * (7 + (unheard_lines / lines_per_sonnet))
    total_sonnets = total_lines / lines_per_sonnet
    result = total_sonnets
    return result

print(solution())