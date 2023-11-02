def solution():
    """It took Dad 5 more than twice as long to vacuum upstairs then to vacuum downstairs. He vacuumed for a total of 38 minutes. How many minutes did he vacuum upstairs?"""
    total_time = 38
    downstairs_time = total_time / 3
    upstairs_time = (2 * downstairs_time) + 5
    result = upstairs_time
    return result

print(solution())