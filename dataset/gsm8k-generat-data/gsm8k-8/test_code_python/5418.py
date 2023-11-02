def solution():
    num_zombies = 480
    days_ago = 0
    while num_zombies >= 50:
        num_zombies /= 2
        days_ago += 1
    result = days_ago
    return result

print(solution())