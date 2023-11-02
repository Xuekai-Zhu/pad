def solution():
    # Calculate the time one kid would need to wash one whiteboard
    time_per_whiteboard = 20/4/3  # 4 kids can wash 3 whiteboards in 20 minutes
    # Calculate the time one kid would need to wash six whiteboards
    time_for_six_whiteboards = time_per_whiteboard * 6
    result = time_for_six_whiteboards
    return result

print(solution())