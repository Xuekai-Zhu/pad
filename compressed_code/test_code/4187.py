def solution():
    
    zombie_count = 480
    days_ago = 0
    while zombie_count >= 50:
        zombie_count /= 2
        days_ago += 1
    result = days_ago
    return result

print(solution())