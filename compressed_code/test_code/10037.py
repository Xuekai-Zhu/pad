def solution():
    
    current_zombies = 480
    days_ago = 0
    while current_zombies >= 50:
        current_zombies /= 2
        days_ago += 1
    result = days_ago
    return result

print(solution())