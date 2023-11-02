def solution():
    """Four kids can wash three whiteboards in 20 minutes. How long would it take, in minutes, for one kid to wash six whiteboards?"""
    kids = 4
    whiteboards = 3
    time = 20
    whiteboards_per_kid = whiteboards / kids
    time_per_whiteboard = time / whiteboards_per_kid
    time_for_six_whiteboards = time_per_whiteboard * 2
    result = time_for_six_whiteboards
    return result

print(solution())