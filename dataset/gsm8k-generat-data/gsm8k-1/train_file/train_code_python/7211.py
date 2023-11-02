def solution():
    """Ravi can jump higher than anyone in the class. In fact, he can jump 1.5 times higher than the average jump of the three next highest jumpers. If the three next highest jumpers can jump 23 inches, 27 inches, and 28 inches, how high can Ravi jump?"""
    top_three_jumpers = [23, 27, 28]
    avg_height = sum(top_three_jumpers) / len(top_three_jumpers)
    ravi_jump = 1.5 * avg_height
    result = ravi_jump
    return result

print(solution())