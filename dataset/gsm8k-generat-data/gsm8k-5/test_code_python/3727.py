def solution():
    drumsticks = 24
    breasts = drumsticks - 4  # Steph bought 4 fewer breast parts than drumsticks

    # Each chicken has 2 parts (drumstick and breast)
    total_chickens = (drumsticks + breasts) // 2

    result = total_chickens
    return result

print(solution())