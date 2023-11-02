def solution():
    num_zombies = 480
    num_days = 0

    while num_zombies >= 50:
        num_days += 1
        num_zombies /= 2

    result = num_days
    return result

print(solution())