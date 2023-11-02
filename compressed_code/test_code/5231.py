def solution():
    
    total_tips = 20 + 60 + 15 + 40
    target_avg = 50
    target_total = 5 * target_avg
    remaining_tips_needed = target_total - total_tips
    result = remaining_tips_needed
    return result

print(solution())