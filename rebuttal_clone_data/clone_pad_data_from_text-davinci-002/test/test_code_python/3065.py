def solution():
    total_zombies = 480
    days = 0
    while total_zombies >= 50:
        total_zombies = total_zombies / 2
        days = days + 1
    result = days
    return result

print(solution())